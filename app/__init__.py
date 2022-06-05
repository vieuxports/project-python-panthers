import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies-josh')
def hobbiesJosh():
    return render_template('hobbies-Josh.html', title="Josh's Hobbies", url=os.getenv("URL"))

@app.route('/hobbies-jul')
def hobbiesJuli():
    return render_template('hobbies-Juli.html', title="Josh's Hobbies", url=os.getenv("URL"))


@app.route('/hobbies-maansi')
def hobbiesMaansi():
    return render_template('hobbies-Maansi.html', title="Josh's Hobbies", url=os.getenv("URL"))