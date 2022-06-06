import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/main/index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies-josh')
def hobbiesJosh():
    return render_template('hobbies-Josh.html', title="Josh's Hobbies", url=os.getenv("URL"))

@app.route('/hobbies-jul')
def hobbiesJuli():
    return render_template('hobbies-Juli.html', title="Josh's Hobbies", url=os.getenv("URL"))


@app.route('/hobbies-maansi')
def hobbiesMaansi():
    return render_template('hobbies-Maansi.html', title="Josh's Hobbies", url=os.getenv("URL"))

@app.route('/work-Josh')
def workJosh():
    return render_template('work-experience-Josh.html', title="Work Experience", url=os.getenv("URL"))

@app.route('/work-Juli')
def workJuli():
    return render_template('work-experience-Juli.html', title="Work Experience", url=os.getenv("URL"))

@app.route('/work-Maansi')
def workMaansi():
    return render_template('work-experience-Maansi.html', title="Work Experience", url=os.getenv("URL"))

@app.route('/jul-travel')
def julTravel():
    return render_template('/juliette/jul-travel.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/maansi-travel')
def manTravel():
    return render_template('maansi-travel.html', url=os.getenv("URL"))

@app.route('/josh-travel')
def joshTravel():
    return render_template('josh-travel.html', url=os.getenv("URL"))