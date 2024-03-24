# Instance of the Flask server

from flask import Flask, render_template, request
from weather import get_current_weather

# waitress is the package which provides server for production use
from waitress import serve

app = Flask(__name__)   # This makes our app a Flask app

@app.route('/')
@app.route('/index')

def index():
    return "Hello World!"

if __name__ == "__main__":
    # app.run(host = "0.0.0.0", port = 8000)    # get local development server warning
    serve(app, host="0.0.0.0", port=8000)

