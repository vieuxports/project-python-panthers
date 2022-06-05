import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



@app.route('/')
def index():
  return render_template('/main/index.html', title="MLH Fellow", url=os.getenv("URL"))

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
