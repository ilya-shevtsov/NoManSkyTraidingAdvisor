import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dayzi\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open('1.png').convert('LA')
img.save('greyscale.png')
img = cv2.imread('1.png')

text = pytesseract.image_to_string(img)
print(text)
