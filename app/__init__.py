import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.data import workExperience, headerInfo, hobbiesList, aboutMe, education

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), headerInfo=headerInfo, aboutMe=aboutMe, education=education, workExperience=workExperience, GOOGLE_MAPS_API=os.getenv("GOOGLE_MAPS_API"))


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), hobbiesList=hobbiesList)