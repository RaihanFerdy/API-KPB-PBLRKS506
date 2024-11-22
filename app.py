import requests
from googletrans import Translator

from flask import Flask, Response, request
from flask_cors import CORS
import json

translator = Translator()
app = Flask(__name__)
CORS(app)

def API():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    fact = response.json().get("fact", "No fact found")
    translated_fact = translator.translate(fact, dest='id')
    data = {
        "fact" : fact,
        "translated_fact" : translated_fact.text
    }
    return data


@app.route('/')
def index():
    index_msg = {
        "message": "Welcome to API Mobile Security PBLRKS506",
        "status": "200",
        "path": request.path
    }
    response = Response(
        response=json.dumps(index_msg, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/fact')
def fact():
    try:
        fact_msg = API()
        response = Response(
            response=json.dumps(fact_msg, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        print(e)
        return {"message":"invalid"}

@app.errorhandler(404)
def not_found(error):
    error_msg = (str(error)).split(": ")
    status, message = error_msg[0].replace(" Not Found", ""), error_msg[1]
    response_message = {
        "message": message,
        "status": status,
        "path": request.path
    }
    response = Response(
        response=json.dumps(response_message, ensure_ascii=False),
        status=404,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8080)