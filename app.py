from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "it_a_secret"
debug = DebugToolbarExtension(app)