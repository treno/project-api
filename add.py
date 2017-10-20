"""
Create an API...
- Use the Flask framework to create a small API that can handle GET requests
- Handle a GET request with two numbers and return the sum of those numbers
- The url that will be used to call your service will look something like this:
http://localhost:5000/add/?param1=4&param2=5
- You will need to do some research to:
(a) get a Flask server running and
(b) implement the GET endpoint to do the calculation
- The actual code required to do this will likely be less than 20 lines of code or so
Knowing what to put in those 20 lines will be the trick
- Resources
	- http://flask.pocoo.org/
	- https://www.google.com/search?q=flask+tutorial
"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome"


@app.route("/add/")
def add():
    param1 = int(request.args.get('param1'))
    param2 = int(request.args.get('param2'))
    result = param1 + param2
    return 'The sum of your inputs = ' + str(result)

if __name__ == "__main__":
    app.run()
