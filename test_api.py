import requests 

#1 . Define API URL and the file to test
API_URL = "http://127.0.0.1:8000/extract-invoice-data/"
IMAGE_PATH = "demoInvoice.png"

#2 prepare and send the request 
#we open the image file in binary read mode 

with open(IMAGE_PATH,"rb") as image_file:
    response = requests.post(API_URL, files ={"file": image_file})

if response.status_code ==200:
    print("API Response:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
