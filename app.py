from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/playlist')
def show_playlist():
    return render_template("playlist.html")

@app.route('/resources')
def show_resources():
        return render_template("resources.html")