#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '''
        <h1>Python Operations with Flask Routing and Views</h1>
'''

# Print string route

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f"<h2>Printed in console: {param}</h2>"

#Count numbers 

@app.route('/count/<int:param>')
def count(param):
    numbers = "<br>".join(str(i) in range(1, param + 1))
    return f"<h2>Counting to {param}</h2><p>{numbers}</p>"

#math operations route

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation =='+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "<h2>Error: Division by zero is not allowed</h2>"
    elif operation == '%':
        result = num1 % num2
    else:
        return "<h2>Error: Invalid operation. Use +, _, *, div, or %</h2>"
    return f"<h2>Result of {num1} {operation} {num2}  {result}</h2>"

if __name__ == '__main__':
    # Run the app directly with the specified port
    app.run(port=5555, debug=True)
