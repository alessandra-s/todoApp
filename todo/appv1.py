from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(name)

@app.route("/")
def home1():
    return'hi there'


if name== "main":
    app.run(debug=True)