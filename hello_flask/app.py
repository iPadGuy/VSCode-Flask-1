from flask import Flask
from flask import render_template, render_template_string
from datetime import datetime
import re

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


def home_old():
    return "<h1>Hello, Flask!</h1>"


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


def hello_there_old(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %B %d, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
