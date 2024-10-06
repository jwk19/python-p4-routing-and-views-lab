#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


# Print string route

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

#Count numbers 

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) in range(1, param + 1))
    return numbers

#math operations route

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed", 400
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation. Use +, -, *, div, or %", 400
    
    return str(result)  # Return plain text result


if __name__ == '__main__':
    # Run the app directly with the specified port
    app.run(port=5555, debug=True)
