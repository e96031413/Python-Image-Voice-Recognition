import pytesseract
from PIL import Image

# open image
image = Image.open(r'C:\Users\Yanwei\Desktop\新增資料夾\chinese.PNG')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)