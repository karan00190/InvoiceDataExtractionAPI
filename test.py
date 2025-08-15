import cv2
import pytesseract

# --- IMPORTANT FOR WINDOWS USERS ---
# You must specify the path to the tesseract.exe file
# This path might be different on your computer
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 1. Load the invoice image
# Make sure 'invoice.png' is in the same folder as your script
image_path = 'demoInvoice.png'
image = cv2.imread(image_path)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# 2. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Use Pytesseract to extract text
# This is the core OCR step
extracted_text = pytesseract.image_to_string(gray_image)

# 4. Print the result
print("--- EXTRACTED TEXT ---")
print(extracted_text)
print("----------------------")