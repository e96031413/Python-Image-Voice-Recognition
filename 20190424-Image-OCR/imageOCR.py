import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
image = Image.open(r"C:\Users\Yanwei\Desktop\test_1.png")
text = pytesseract.image_to_string(image)
print(text)