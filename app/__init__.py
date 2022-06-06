import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/main/index.html', title="Python Panthers Portfolio", url=os.getenv("URL"))

@app.route('/hobbies-josh')
def hobbiesJosh():
    return render_template('/joshua/hobbies-Josh.html', title="Josh's Hobbies", url=os.getenv("URL"))

@app.route('/hobbies-jul')
def hobbiesJuli():
    return render_template('/juliette/hobbies-Juli.html', title="Josh's Hobbies", url=os.getenv("URL"))


@app.route('/hobbies-maansi')
def hobbiesMaansi():
    return render_template('/maansi/hobbies-Maansi.html', title="Josh's Hobbies", url=os.getenv("URL"))

@app.route('/work-Josh')
def workJosh():
    return render_template('/joshua/work-experience-Josh.html', title="Work Experience", url=os.getenv("URL"))

@app.route('/work-Juli')
def workJuli():
    return render_template('/juliette/work-experience-Juli.html', title="Work Experience", url=os.getenv("URL"))

@app.route('/work-Maansi')
def workMaansi():
    return render_template('/maansi/work-experience-Maansi.html', title="Work Experience", url=os.getenv("URL"))

@app.route('/jul-travel')
def julTravel():
    return render_template('/juliette/jul-travel.html', url=os.getenv("URL"))

@app.route('/maansi-travel')
def manTravel():
    return render_template('/maansi/maansi-travel.html', url=os.getenv("URL"))

@app.route('/joshua-travel')
def joshTravel():
    return render_template('/joshua/josh-travel.html', url=os.getenv("URL"))

@app.route('/jul-education')
def julEducation():
    return render_template('education.html', uni="McGill University", fact="My school just celebrated its bicentennial", pic1='/img/mcgill1.jpg',pic2='img/mcgill.jpeg', map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2796.2627839218294!2d-73.57933978516613!3d45.50478843875644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cc91a46510f9635%3A0xdde4da9200a4ae74!2sMcGill%20University!5e0!3m2!1sen!2sca!4v1654372237772!5m2!1sen!2sca",url=os.getenv("URL"))

@app.route('/josh-education')
def joshEducation():
    return render_template('education.html', uni="Metropolitan State University", fact="For my first 2 years of college I attended North Hennepin Community College", pic1='/img/metro-state1.jpg',pic2='img/metro-state2.jpg', map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3357.5282368703533!2d-93.07554216879792!3d44.95721633625194!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87f7d561be333d1b%3A0xc6e9943893ee45fb!2sMetropolitan%20State%20University!5e0!3m2!1sen!2sca!4v1654398613843!5m2!1sen!2sca",url=os.getenv("URL"))

@app.route('/maansi-education')
def manEducation():
    return render_template('education.html', uni="University of Michigan", fact="I went to Novi High School in Novi, MI", pic1='/img/u-mich.jpg',pic2='img/u-mich2.jpg', map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2952.0224758585864!2d-83.74041278454628!3d42.278043579192584!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x883cae38e7de1701%3A0x5ba14e5178e997e3!2sUniversity%20of%20Michigan!5e0!3m2!1sen!2sca!4v1654400474561!5m2!1sen!2sca",url=os.getenv("URL"))
