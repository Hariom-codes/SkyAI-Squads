import os, shutil
from pathlib import Path
import pytesseract
from PIL import Image, ImageOps, ImageFilter
from pdf2image import convert_from_bytes, pdfinfo_from_bytes
try:
    import pymupdf as fitz
except ImportError:
    fitz = None
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parents[1] / '.env')
except Exception:
    pass

def _first_existing(paths):
    for raw in paths:
        if raw and Path(raw).exists(): return str(raw)
    return None

def _configure_tesseract():
    candidates=[os.getenv('TESSERACT_CMD'),os.getenv('TESSERACT_PATH'),shutil.which('tesseract'),r'C:\Program Files\Tesseract-OCR\tesseract.exe',r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',str(Path.home()/'AppData/Local/Programs/Tesseract-OCR/tesseract.exe')]
    found=_first_existing(candidates)
    if found: pytesseract.pytesseract.tesseract_cmd=found
    return found

def _configure_poppler():
    candidates=[os.getenv('POPPLER_PATH'),shutil.which('pdftoppm'),r'C:\Program Files\poppler\Library\bin',r'C:\Program Files\poppler\bin']
    for raw in candidates:
        if not raw: continue
        p=Path(raw)
        if p.is_file(): p=p.parent
        if p.exists() and ((p/'pdftoppm.exe').exists() or (p/'pdfinfo.exe').exists()): return str(p)
    return None
TESSERACT_PATH=_configure_tesseract(); POPPLER_PATH=_configure_poppler()

def _ocr_image(image):
    gray=ImageOps.autocontrast(ImageOps.grayscale(image)).filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(gray, config='--psm 6')

def extract_text_from_image(image_path):
    if not TESSERACT_PATH: raise RuntimeError('Tesseract OCR is not available. Set TESSERACT_CMD in backend/.env or install Tesseract OCR.')
    with Image.open(image_path) as image: return _ocr_image(image)

def extract_text_from_pdf(pdf_bytes):
    """Fast path: extract embedded PDF text. OCR only genuinely scanned/empty pages."""
    if fitz is not None:
        doc=fitz.open(stream=pdf_bytes,filetype='pdf'); texts=[]; scanned=[]
        for i,page in enumerate(doc):
            text=page.get_text('text').strip(); texts.append(text)
            if len(text)<40: scanned.append(i)
        if scanned and not TESSERACT_PATH:
            doc.close(); raise RuntimeError('This PDF appears to be scanned and Tesseract OCR is not available.')
        for i in scanned:
            page=doc.load_page(i); pix=page.get_pixmap(matrix=fitz.Matrix(200/72,200/72),alpha=False)
            image=Image.frombytes('RGB',[pix.width,pix.height],pix.samples); texts[i]=_ocr_image(image).strip()
        doc.close(); return '\n\n'.join(texts)
    if not TESSERACT_PATH: raise RuntimeError('Tesseract OCR is not available. Install PyMuPDF or configure Tesseract OCR.')
    pages=convert_from_bytes(pdf_bytes,poppler_path=POPPLER_PATH,dpi=200)
    return '\n'.join(_ocr_image(page) for page in pages)

def get_pdf_page_count(pdf_bytes):
    if fitz is not None:
        doc=fitz.open(stream=pdf_bytes,filetype='pdf'); n=doc.page_count; doc.close(); return n
    return int(pdfinfo_from_bytes(pdf_bytes,poppler_path=POPPLER_PATH).get('Pages',0))
