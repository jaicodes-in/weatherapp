from flask import Flask, request, render_template,jsonify

app=Flask(__name__)

@app.route('/')
def homepagefunction():
    return render_template('index_weather.html')

@app.route('/weatherapp')
def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {'q' :"delhi",
          'appid' : apikey,
          'units':'metric'}
    response = requests.get(url, params=param)
    data=response.json()
    return f"data:{data}"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8003)