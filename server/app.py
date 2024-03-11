#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:int>')
def count(int):
    string = f""
    for num in range(int):
        string += (f"{str(num)}\n")
    return(string)

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num2)
    num2 = int(num2)
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
