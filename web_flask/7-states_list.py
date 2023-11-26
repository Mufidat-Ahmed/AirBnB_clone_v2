#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a HTML page: (inside the tag BODY)"""
    states = storage.all("States")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exec):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
