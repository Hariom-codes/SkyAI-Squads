from pathlib import Path
from fastapi import APIRouter, Request
from api.auth import current_user_from_request

router = APIRouter(prefix="/knowledge-base", tags=["Knowledge Base"])
BASE_DIR = Path(__file__).resolve().parent.parent
KB_DIR = BASE_DIR / "data" / "Tata_Legal_Knowledge_Base_Complete_30_PDFs"


def _category(path: Path):
    return path.parent.name.replace("_", " ").title()


@router.get("")
def knowledge_base(request: Request):
    current_user_from_request(request)
    files = []
    for path in sorted(KB_DIR.rglob("*.pdf")):
        rel = path.relative_to(KB_DIR)
        files.append({"id": path.stem, "name": path.name, "category": _category(path), "path": str(rel).replace("\\", "/"), "size_kb": round(path.stat().st_size / 1024, 1)})
    return {"name": "SkyAI-Legal Knowledge Base", "count": len(files), "files": files}
