# CST 205
# William Hurley
# July 7, 2024
# Git Link: 

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')

# def hello():
#     return 'Hello, World!'

@app.route('/william')
def template():
    return render_template('template.html')
