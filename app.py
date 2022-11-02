from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SECRET_KEY'] = '6uar1n0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

#seed database
#seed_db(app)

#old unnecessary with seeding db above
with app.app_context():
    db.create_all()


@app.route('/')
def homepage_route():
    """default homepage route"""

    return render_template("index.html")