from flask import Flask, render_template
import pandas as pd

car=pd.read_csv('cleaned Car.csv')

app = Flask(__name__)

@app.route('/')
def hello_world():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique())
    fuel_type = car['fuel_type'].unique()
    return render_template('index.html',companies=companies,car_models=car_models,year=year,fuel_type=fuel_type)
    # return 'Hello, World!'

@app.route('/products')
def products():
    return 'This is productcts page'

if __name__=="__main__":
    app.run(debug=True)