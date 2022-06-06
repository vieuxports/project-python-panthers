import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/main/index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/jul-travel')
def julTravel():
    return render_template('/juliette/jul-travel.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/maansi-travel')
def manTravel():
    return render_template('/maansi/maansi-travel.html', url=os.getenv("URL"))

@app.route('/josh-travel')
def joshTravel():
    return render_template('/joshua/josh-travel.html', url=os.getenv("URL"))