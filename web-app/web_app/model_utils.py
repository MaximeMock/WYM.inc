import requests

def predict(text):
    url = 'http://0.0.0.0:8000/model/predict'
    text_json = {"text": text}
    output_json = requests.post(url, json = text_json)
    output = output_json['summary_text']
    return output