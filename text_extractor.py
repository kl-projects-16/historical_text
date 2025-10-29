import pytesseract
from PIL import Image
import os


def extract_text_from_image(image_path):
    """Extract text from a given image path using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text

