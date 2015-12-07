from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db
import doctest

app = Flask(__name__)

app.secret_key = "darling"

app.jinja_env.undefined = StrictUndefined


if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run()

    # doctest.testmod(verbose=True)
