# Dependencies

from flask import Flask, request, jsonify
import joblib

import pandas as pd

# Your API definition
app = Flask(__name__)

@app.route("/")
def hello():
    return "I'm an API for predictions"
