# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:52:37 2022

@author: Ulises Reveles
"""

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "abcEERE##$1@"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    flash("Hi " + str(request.form['name_input']) + ", it is great to see you!")
    return render_template("index.html")

