from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
import json
import collections

from helpers import apology

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/coursetimes", methods=["GET"])
def coursetimes():
    with open("data/new_coursetimes.json") as json_data:
        d = json.load(json_data, object_pairs_hook=collections.OrderedDict)
    return json.dumps([d])


@app.route("/concentrations", methods=["GET"])
def concentrations():
    with open("data/StudentConcentrations.json") as json_data:
        d = json.load(json_data)
    return jsonify(d)


@app.route("/AthleteConcentrations", methods=["GET"])
def athleteConcentrations():
    with open("scrapers/A_Concentrations.json") as json_data:
        f = json.load(json_data)
    return jsonify(f)


@app.route("/data", methods=["GET"])
def data():
    return render_template("data.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/team", methods=["GET"])
def team():
    return render_template("team.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
