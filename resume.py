from flask import Flask
from flask import request
from flask import render_template
import solr
import re
from sqliteOperation import sqliteTable

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("resume.html")

@app.route('/', methods=['POST'])
def my_form_post():
    # create a connection to a solr server
    s = solr.Solr('http://localhost:8983/solr/resume_core')

    # doc = dict(
    #     id=1,
    #     name='Chris Cahill',
    #     resume_text="Java Python",
    # )
    # s.add(doc, commit=True)

    r_text = request.form['r_text']
    d_text = request.form['d_text']
    query_string = ""
    r = r_text.split(",")
    if len(r) == 1 and r[0].strip():
        query_string = 'resume_text:' + r[0].strip()
    elif len(r) > 1:
        counter = 1
        query_string = 'resume_text:('
        for skill in r:
            if counter == len(r):
                query_string = query_string + '"' + skill + '")'
            else:
                query_string = query_string + '"' + skill + '" AND '
            counter = counter + 1
    print(query_string)
    response = s.select(query_string)
    r_results = response.results
    results = {}
    for result in r_results:
        results[result['id']] = result

    d = d_text.split(",")
    d_results = None
    if len(d) == 1 and d[0].strip():
        query_string = 'resume_text:' + d[0].strip()
        print(query_string)
        response = s.select(query_string)
        d_results = response.results
    elif len(d) > 1:
        counter = 1
        query_string = 'resume_text:('
        for skill in d:
            if counter == len(d):
                query_string = query_string + '"' + skill + '")'
            else:
                query_string = query_string + '"' + skill + '" OR '
            counter = counter + 1
        print(query_string)
        response = s.select(query_string)
        d_results = response.results

    good_desired_results = []
    if len(r_results) > 0:
        if d_results:
            for result in d_results:
                if result['id'] in results.keys():
                    good_desired_results.append(result)
            for result in good_desired_results:
                old_result = results[result['id']]
                old_result['score'] = old_result['score'] + result['score']
                results[result['id']] = old_result

        combined_result = []
        db = sqliteTable()
        for result in results.values():
            combined = {}
            id = int(result['id'])
            relational_result = db.queryID([id])
            for ele in relational_result:
                combined['name'] = ele[1].encode('utf-8')
                combined['university'] = ele[2].encode('utf-8')
                combined['major'] = ele[3].encode('utf-8')
                combined['gpa'] = ele[4].encode('utf-8')
                combined['pdf_path'] = result['pdf_path'][0].encode('utf-8')
                combined_result.append(combined)
        return render_template('results.html', responses=combined_result)
    else:
        return render_template('results.html', responses=d_results)

if __name__ == '__main__':
    app.run()