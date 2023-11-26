#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page (filters page)"""
    states = storage.all("States")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states,
            amenities=amenities)


@app.teardown_appcontext
def teardown(exec):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
