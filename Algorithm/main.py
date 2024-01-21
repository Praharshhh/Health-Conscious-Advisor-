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
