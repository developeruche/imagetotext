from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe'

image = Image.open("test3.png")
text = tess.image_to_string(image)

print(text)
