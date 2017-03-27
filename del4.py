import json
import requests
from flask import Flask ,jsonify , request


app = Flask(__name__)

languages = [{'us': 'english'} , {'india' : 'tamil'}, {'thailand':'thai'}]

@app.route('/')
def main():
    return jsonify('welcome')

@app.route('/lang' , methods=['GET'])
def lang():
    return jsonify(languages)

@app.route('/lang' , methods=['POST'])
def addone():
    language ={'name' : requests.json['name']}

    languages.append(language)


    return jsonify({'languages' : languages})





if __name__ == ('__main__'):
    app.run(debug=True)
