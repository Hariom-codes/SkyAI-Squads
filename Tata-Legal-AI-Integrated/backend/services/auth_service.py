import base64
import hashlib
import hmac
import os
import secrets
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "security.db"
TOKEN_TTL_SECONDS = int(os.getenv("TOKEN_TTL_SECONDS", "28800"))
SECRET = os.getenv("AUTH_SECRET", "")


def _secret():
    global SECRET
    if not SECRET:
        SECRET = os.getenv("AUTH_SECRET") or secrets.token_hex(32)
    return SECRET.encode("utf-8")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def init_db():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            display_name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'reviewer',
            created_at TEXT NOT NULL,
            last_login TEXT
        )""")
        conn.commit()


def _hash_password(password: str, salt: bytes | None = None):
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2**14, r=8, p=1)
    return f"scrypt${base64.urlsafe_b64encode(salt).decode()}${base64.urlsafe_b64encode(digest).decode()}"


def _verify_password(password: str, stored: str):
    try:
        _, salt_b64, digest_b64 = stored.split("$", 2)
        salt = base64.urlsafe_b64decode(salt_b64.encode())
        expected = base64.urlsafe_b64decode(digest_b64.encode())
        actual = hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2**14, r=8, p=1)
        return hmac.compare_digest(actual, expected)
    except Exception:
        return False


def create_user(username: str, password: str, display_name: str, role: str = "reviewer"):
    init_db()
    username = username.strip().lower()
    display_name = display_name.strip() or username
    if len(username) < 3 or len(password) < 8:
        raise ValueError("Username must be at least 3 characters and password at least 8 characters.")
    password_hash = _hash_password(password)
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.execute(
                "INSERT INTO users (username, display_name, password_hash, role, created_at) VALUES (?, ?, ?, ?, ?)",
                (username, display_name, password_hash, role, now_iso()),
            )
            user_id = cur.lastrowid
            conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists.")
    return {"id": user_id, "username": username, "display_name": display_name, "role": role}


def ensure_admin():
    init_db()
    username = os.getenv("ADMIN_USERNAME", "hariom").strip().lower()
    password = os.getenv("ADMIN_PASSWORD", "SkyAI-Admin-2026!")
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute("SELECT id FROM users WHERE username=?", (username,)).fetchone()
    if not row:
        create_user(username, password, "Hariom Upadhyay", "admin")


def authenticate(username: str, password: str):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM users WHERE username=?", (username.strip().lower(),)).fetchone()
        if not row or not _verify_password(password, row["password_hash"]):
            return None
        conn.execute("UPDATE users SET last_login=? WHERE id=?", (now_iso(), row["id"]))
        conn.commit()
        return {"id": row["id"], "username": row["username"], "display_name": row["display_name"], "role": row["role"]}


def _b64(value: bytes):
    return base64.urlsafe_b64encode(value).rstrip(b"=").decode("ascii")


def issue_token(user: dict):
    payload = f"{user['id']}|{user['username']}|{user['role']}|{int(time.time()) + TOKEN_TTL_SECONDS}"
    encoded = _b64(payload.encode())
    signature = _b64(hmac.new(_secret(), encoded.encode(), hashlib.sha256).digest())
    return f"{encoded}.{signature}"

def verify_token(token: str):
    try:
        encoded, signature = token.split(".", 1)

        expected = _b64(
            hmac.new(
                _secret(),
                encoded.encode(),
                hashlib.sha256
            ).digest()
        )

        if not hmac.compare_digest(signature, expected):
            return None

        payload = base64.urlsafe_b64decode(
            encoded + "=" * (-len(encoded) % 4)
        ).decode()

        user_id, username, role, exp = payload.split("|", 3)

        if int(exp) < int(time.time()):
            return None

        # Get complete user information from database
        init_db()

        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row

            row = conn.execute(
                """
                SELECT id, username, display_name, role
                FROM users
                WHERE id = ? AND username = ?
                """,
                (int(user_id), username)
            ).fetchone()

        if not row:
            return None

        return {
            "id": row["id"],
            "username": row["username"],
            "display_name": row["display_name"],
            "role": row["role"],
            "exp": int(exp),
        }

    except Exception:
        return None


def list_users():
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT id, username, display_name, role, created_at, last_login FROM users ORDER BY id").fetchall()
        return [dict(r) for r in rows]


def security_summary():
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    return {"users": users, "token_ttl_seconds": TOKEN_TTL_SECONDS, "password_hash": "scrypt", "audit_logging": True}
