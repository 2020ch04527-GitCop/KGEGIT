import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set the tesseract executable path if needed (uncomment and update if not in PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def preprocess_image(image_path):
    """
    Preprocess the image for better OCR results.
    Steps: grayscale, thresholding (Otsu's), can be extended for denoising, etc.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def ocr_kannada(image_path):
    """
    Run Tesseract OCR on the preprocessed image using Kannada language.
    """
    img = preprocess_image(image_path)
    pil_img = Image.fromarray(img)
    text = pytesseract.image_to_string(pil_img, lang='kan')
    return text

if __name__ == "__main__":
    image_path = "kannada_sample.png"  # Replace with your image file
    result = ocr_kannada(image_path)
    print("Recognized Kannada Text:")
    print(result)
