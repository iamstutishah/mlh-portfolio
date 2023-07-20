import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.data import workExperience, headerInfo, hobbiesList, aboutMe, education, skills
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()
app = Flask(__name__)

# In-memory instance of the database
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', 
    uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=3306
        )

# Database
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

print(mydb)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), headerInfo=headerInfo, aboutMe=aboutMe, education=education, workExperience=workExperience, skills=skills)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), hobbiesList=hobbiesList)


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    # name = request.form['name']
    # email = request.form['email']
    # content = request.form['content']
    # timeline_post = TimelinePost.create(name=name, email=email, content=content)
    try:
         name = request.form['name']
    except Exception as e:
        return "Invalid name", 400
    else:
        if name == '':
            return "Invalid name", 400

    try:
        email = request.form['email']
    except Exception as e:
        return "Invalid email", 400
    else:
        if email == '':
            return "Invalid email", 400

    try:
        content = request.form['content']
    except Exception as e:
        return "Invalid content", 400
    else:
        if content == '':
            return "Invalid content", 400

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline", url=os.getenv("URL"))




