
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Area':'Jharkand', 'Oxygen':40, 'Temperature':45, 'Humidity':20, 'Fire Occurrence':1})

print(r.json())