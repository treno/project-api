"""
Create an API...
- Use the Flask framework to create a small API
- Should handle a GET request with two numbers and return the sum
- The url used to call your service will look something like: http://localhost:5000/add/?param1=4&param2=5
- You will need to do some research to:
    (a) get a Flask server running and
    (b) implement the GET endpoint to do the calculation
- The actual code required to do this will likely be less than 20 lines of code or so
- Knowing what to put in those 20 lines will be the trick
- Resources
    - http://flask.pocoo.org/
    - https://www.google.com/search?q=flask+tutorial
"""
# launches a simple API that handles integer additions via a built-in server
from flask import Flask
from flask import request
# create an instance of the Flask class
app = Flask(__name__)


# use the route() decorator to tell Flask what URL should trigger our function
# function returns a text string to greet the user
@app.route("/")
def index():
    return "Welcome, Craig and Tom!"


# uses the route() decorator to tell Flask what URL should trigger our function
# function returns the sum of input parameters specified by user
@app.route("/add/")
def add():
    try:
        param1 = int(request.args.get("param1"))
        param2 = int(request.args.get("param2"))
        result = param1 + param2
        return "The sum of your inputs = " + str(result)
    except ValueError:
        return "You seem to have entered a bad value...try again, but this time only use integers!"
    else:
        return "Uh oh, there seems to have been an error!"


if __name__ == "__main__":
    app.run()
