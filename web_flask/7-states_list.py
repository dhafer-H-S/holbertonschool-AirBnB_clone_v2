#!/usr/bin/python3
"""script that starts a Flask web application"""
import models
from flask import Flask, abort, render_template
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_route():
    """Display the states in order”"""
    states = models.storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
