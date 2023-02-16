from flask import Flask
import os
import random

app = Flask(__name__)

@app.route('/naman')
def hello_world():
    return 'Hello, Docker!'
@app.route('/dock')
def naman():
    return "Finally we did it atlast"
app.run(host="0.0.0.0")
