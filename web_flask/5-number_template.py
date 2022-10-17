#!/usr/bin/python3
"""
Simple flask app
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    / - route: display “Hello HBNB!”
    """
    return("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    /hbnb - route: display “HBNB”
    """
    return("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    /hbnb - route: display "url variable"
    """
    body = text.replace('_', ' ')
    return(f"C {body}")

@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    /hbnb - route: display "url variable"
    """
    body = text.replace('_', ' ')
    return(f"Python  {body}")

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    /hbnb - route: display "url variable"
    """
    if isinstance(n, int):
        return(f"{n} is a number")

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    /hbnb - route: return template with "url variable"
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)



if __name__ == "__main__":
        app.run(
                host="0.0.0.0",
                port=5000
        )