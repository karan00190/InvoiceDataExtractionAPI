import cv2
import pytesseract

# For Windows Users: Update this path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 1. Load the image
image_path = 'demoInvoice.png'
image = cv2.imread(image_path)

# 2. --- IMAGE PREPROCESSING ---
# a. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# b. Convert to black and white (this is called thresholding)
# This step makes the text stand out sharply from the background.
_, processed_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 3. Perform OCR on the CLEANED image
extracted_text = pytesseract.image_to_string(processed_image)

# 4. Print the result
print("--- Improved Extracted Text ---")
print(extracted_text)
print("-----------------------------")