from flask import Flask, request, render_template, redirect, url_for, flash
import os
import secrets

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("ex1.html",name='Jinjia2模板')

# @app.route('/hello')
# def hello_world():  # put application's code here
#     return 'Hello World!'

# @app.route('/index')
# def index():  # put application's code here
#     if request.method == 'GET':
#         return render_template('index.html')


if __name__ == '__main__':
    app.run()
