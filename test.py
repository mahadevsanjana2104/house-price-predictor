import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "bedrooms": 3,
    "bathrooms": 2,
    "living_area": 1500,
    "floors": 2
}

res = requests.post(url, json=data)
print(res.text)