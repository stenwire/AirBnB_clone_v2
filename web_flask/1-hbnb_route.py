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


if __name__ == "__main__":
        app.run(
                host="0.0.0.0",
                port=5000
        )
