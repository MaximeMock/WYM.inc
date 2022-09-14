import requests

def predict(text):
    url = 'http://Model_ML:5000/model/predict'
    text_json = {"text": [text]}
    output_first = requests.post(url, json = text_json)
    output_json = output_first.json()
    output = output_json['summary_text'][0]
    return output