import requests
from flask import Flask , render_template , request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def main():
    return render_template('city_new.html')

@app.route('/temperature' , methods = ['POST'])
def temperature ():
    try:
        zipcode = request.form['zip']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+zipcode+'&appid=50e60faf87e4d6334ee0b6a87921592b')
        print (r)
        
        json_object = r.json()
        city_name = json_object['name']
        city_temp = json_object['main']['temp']
        city_far = (city_temp - 273.15) *1.8 +32
        return render_template('city.html' , temp=city_far , area_name = city_name)
    except KeyError :
        return render_template('error.html')


if (__name__) == ('__main__'):
    app.run(debug=True)
