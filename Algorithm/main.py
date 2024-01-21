from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/food-suggestions', methods=['POST'])
def test():
    if request.method != 'POST':
        return "Request method must be 'POST' request"

    try:
       data = request.get_json()
       print(data)

    except Exception as err:
        print(err)
        return "ERROR"

    return "Image Recived"


#here we will use postman of the forentend to make it work with the backend 
http://127.0.0.1:5000/food-suggestions
