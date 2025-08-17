# AI-Powered Invoice Data Extraction API

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)

This project is an end-to-end pipeline that automates the extraction of structured data (like Invoice ID, Billed To, Due Date, and Amount Due) from unstructured invoice documents. It leverages OCR and a custom-trained Named Entity Recognition (NER) model, exposing the functionality through a high-performance REST API built with FastAPI.



## ## Workflow Architecture

The application follows a simple, robust pipeline for processing each document:

```
Image Upload --> FastAPI Server --> OCR (Pytesseract) --> Custom NER Model (spaCy) --> Structured JSON Output
```

## ## Key Features

-   **Automated Text Extraction:** Uses Pytesseract for Optical Character Recognition (OCR) to extract raw text from image-based invoices.
-   **Custom NLP Model:** Features a custom Named Entity Recognition (NER) model built with spaCy, trained specifically to identify key entities on invoices.
-   **RESTful API:** Provides a clean, fast, and scalable API endpoint built with FastAPI for real-time data extraction.
-   **End-to-End Pipeline:** Demonstrates a complete machine learning project lifecycle from data annotation and model training to deployment as a microservice.

---
## ## Tech Stack

-   **Backend:** FastAPI
-   **Server:** Uvicorn
-   **Machine Learning:** spaCy
-   **OCR:** Pytesseract
-   **Image Processing:** OpenCV
-   **Core Language:** Python 3.11+

---
## ## Setup and Installation

Follow these steps to set up the project locally.

**1. Clone the Repository**
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

**2. Install Tesseract OCR**
You must install Google's Tesseract engine on your system. Follow the instructions for your OS:
-   [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)

**3. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**4. Install Dependencies**
```bash
pip install -r requirements.txt
```

---
## ## Usage

The project is split into two main steps: training the model and running the API.

**1. Train the Custom NER Model**
Run the training script. This will create the `my_invoice_model` directory containing your trained model.
```bash
python custom_ner_training.py
```

**2. Run the API Server**
Start the FastAPI application using Uvicorn.
```bash
uvicorn main:app --reload
```
The API will now be running at `http://127.0.0.1:8000`.

---
## ## API Endpoint

You can test the API using the interactive documentation provided by FastAPI.

-   **URL:** `http://127.0.0.1:8000/docs`

### Extract Invoice Data

-   **Endpoint:** `POST /extract-invoice-data/`
-   **Description:** Uploads an invoice image for data extraction.
-   **Request Body:** `multipart/form-data` containing the image file.
-   **Successful Response (200 OK):**

```json
{
  "filename": "demoInvoice.png",
  "extracted_data": {
    "BILLED_TO": "Sarthak Mittal",
    "INVOICE_ID": "806",
    "DUE_DATE": "25992020",
    "AMOUNT_DUE": "Anoum Due (USD)"
  }
}
```
