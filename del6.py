from flask import Flask , render_template , request
import requests
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def main():
    return render_template('index1.html')


@app.route('/temperature' , methods = ['POST'])
def temperature ():
    try:
        zipcode = request.form['zip']
        r =  requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=50e60faf87e4d6334ee0b6a87921592b')
        json_object = r.json()
        name = json_object['name']
        temp_k = float(json_object['main'] ['temp'])
        #return str(temp_k)
        return render_template('temperature.html' , temp=temp_k , area_name = name)
    except KeyError :
        return render_template('error.html')


if (__name__) == ('__main__'):
    app.run(debug=True)
