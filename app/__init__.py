import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.data import workExperience, headerInfo, hobbiesList

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), headerInfo=headerInfo, workExperience=workExperience)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), hobbiesList=hobbiesList)