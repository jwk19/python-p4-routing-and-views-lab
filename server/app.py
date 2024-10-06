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
    try:
        # Check if the parameter is valid (non-negative)
        if param < 0:
            return "Error: Parameter must be a non-negative integer.", 400
        
        # Generate the numbers as plain text, separated by newlines
        numbers = "\n".join(str(i) for i in range(param))  # Range starts from 0 to param-1
        return numbers, 200  # Return as plain text with status code 200
    
    except Exception as e:
        # Log the exception for debugging
        print(f"Error in count route: {e}")
        return "Internal Server Error", 500


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
