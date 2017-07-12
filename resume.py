from flask import Flask
from flask import request
from flask import render_template
import solr
import re

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("resume.html")

@app.route('/', methods=['POST'])
def my_form_post():
    # create a connection to a solr server
    s = solr.Solr('http://localhost:8983/solr/resume_core')

    r_text = request.form['r_text']
    d_text = request.form['d_text']
    print("Required: " + r_text)
    print("Desired: " + d_text)

    r = r_text.split(",")
    d = d_text.split(",")
    skills = r + d
    print(skills)

    # do a search
    query_string = 'resume_text:' + skills[0].strip()
    print(query_string)
    response = s.select(query_string)
    print("hi")

    return render_template('resume.html', responses=response.results)

if __name__ == '__main__':
    app.run()