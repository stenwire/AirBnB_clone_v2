#!/usr/bin/python3
"""
Simple flask app
"""

from flask import Flask

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
    /c_route - route: display "url variable"
    """
    body = text.replace('_', ' ')
    return("C {}".format(body))


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    /hbnb - route: display "url variable"
    """
    body = text.replace('_', ' ')
    return("Python {}".format(body))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
