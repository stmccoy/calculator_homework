from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/<num_1>/<num_2>')
def add(num_1, num_2):
    return render_template('add.html', num_1 = float(num_1), num_2 = float(num_2), answer = float(num_1) + float(num_2))

@app.route('/divide/<num_1>/<num_2>')
def divide(num_1, num_2):
    return render_template('divide.html', num_1 = float(num_1), num_2 = float(num_2), answer = float(num_1) / float(num_2))

@app.route('/multiply/<num_1>/<num_2>')
def multiply(num_1, num_2):
    return render_template('multiply.html', num_1 = float(num_1), num_2 = float(num_2), answer = float(num_1) * float(num_2))

@app.route('/subtract/<num_1>/<num_2>')
def subtract(num_1, num_2):
    return render_template('subtract.html', num_1 = float(num_1), num_2 = float(num_2), answer = float(num_1) - float(num_2))

