# input_module/ocr_extractor.py

import pytesseract
from PIL import Image, ImageFilter, ImageOps

def extract_handwritten_text(image_path: str) -> dict:
    """
    Extracts text from a handwritten answer sheet using OCR.
    """
    img = Image.open(image_path)

    # Preprocessing: convert to grayscale, increase contrast, binarize
    img = img.convert("L")  # Grayscale
    img = ImageOps.autocontrast(img)
    img = img.point(lambda x: 0 if x < 140 else 255)  # Binarization

    raw_text = pytesseract.image_to_string(img)

    print("=== OCR RAW OUTPUT ===")
    print(raw_text)

    answers = {}
    for line in raw_text.split('\n'):
        if ":" in line:
            parts = line.strip().split(":", 1)
            if len(parts) == 2:
                qid, ans = parts
                answers[qid.strip()] = ans.strip()
    return answers
