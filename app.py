from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from sqliteOperation import sqliteTable
 
app = app = Flask(__name__, template_folder='hackathon webisite/')

 
@app.route("/hello/<string:name>/")
def hello(name):
#    return name
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
 
    return render_template(
        'test.html',**locals())

@app.route("/sqlDemo/")
def sql():
    db = sqliteTable()
    list = db.queryID([1, 2, 3, 4, 5])
    records = []
    for ele in list:
        record = []
        record.append(ele[1].encode('utf-8'))
        record.append(ele[2].encode('utf-8'))
        record.append(ele[3].encode('utf-8'))
        record.append(ele[4].encode('utf-8'))
        records.append(record)
    return render_template(
        'index_yiming.html', records=records)







 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
