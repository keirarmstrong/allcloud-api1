import flask
from flask import Flask
import os
import settings

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Under development."
