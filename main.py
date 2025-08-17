import cv2
import pytesseract
import spacy
import numpy as np
from fastapi import FastAPI, UploadFile, File

#1 Initialize the application

app = FastAPI(title ="Invoice Extraction API")

#2. set tesseract path and load the custom model

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try: 
    nlp_custom = spacy.load("./my_invoice_model")
    print("Custom NER model loaded successfully.")
except IOError:
    print("Error : Custom model not found !.. Run custom_ner_training.py first and then try again")
    nlp_custom = None

#3. Define the API Endpoint 

@app.post("/extract-invoice-data/")
async def extract_invoice_data(file: UploadFile =File(...)):
    
    #This function defines the main pipeline of the application
    if not nlp_custom:
        return {"error":"Custom NER model is not available."}
    # a. Read the image from the uploaded file.

    contents = await file.read()

    # b. convert the file content to an openCV image format
    np_arr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # c. Perform OCR using Pytesseract to get raw text.
    extracted_text = pytesseract.image_to_string(image)

    # d. Feed the raw text to your custom spaCy model to find entities.
    doc = nlp_custom(extracted_text)

    #e . Loop through the found entities and format them into a dictionary.

    results ={}
    for ent in doc.ents:
        results[ent.label_] = ent.text.strip()
    

    return{
        "filename" : file.filename,
        "extracted_data": results
    }




