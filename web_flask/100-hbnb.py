#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays a HTML page: (filters page)"""
    states = storage.all("States")
    amenities = storage.all("Amenity")
    places = storage.all("Places")
    return render_template("100-hbnb.html", states=states,
            amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exec):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
