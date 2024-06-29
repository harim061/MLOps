import requests
import json

url = "http://localhost:5001/predict" 

data = {
    "Cylinders": 8,
    "Displacement": 390.0,
    "Horsepower": 190,
    "Weight": 3850,
    "Acceleration": 8.5,
    "ModelYear": 70,
    "Country": "USA",
}

input_data = json.dumps(data)
headers = {"Content-Type": "application/json"}
resposne = requests.post(url, input_data, headers=headers)
print(resposne.text)