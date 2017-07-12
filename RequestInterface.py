# importing the requests library
import requests
import json
import csv
from sets import Set

def ReadTextFiles(fileName):
    with open(fileName, "r") as myfile:
        data = myfile.read()
        return data

def GetEntityResult(str):
    ENDPOINT = "https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyAofEz7JEguPw8PGMwKeleaJt4XEVmjkmQ"
    data = {
      "encodingType": "UTF8",
      "document": {
        "type": "PLAIN_TEXT",
        "content": str
      }
    }
    r = requests.post(url = ENDPOINT, json=data)
    data = json.loads(r.text)
    return data

def SearchEntity(ResultJSON, entity):
    Result = []
    length = len(ResultJSON[u'entities'])
    for i in range(length):
        entry = ResultJSON[u'entities'][i]

def ParseCSVandSaveMajors():
    return;

def File_Reader(file_obj):
    All_Majors = []
    for line in f_obj:
        #print line
        All_Majors.append(line.rstrip())
    return All_Majors

SearchEntity(GetEntityResult(ReadTextFiles("samples/output.txt")),"PERSON")
All_Majors = []
with open("majors.txt") as f_obj:
    All_Majors = File_Reader(f_obj)


for major in All_Majors:
    #print major.lower()
    str = major.lower()
    searchfile = open("samples/output_13.txt", "r")
    for line in searchfile:
        if major.lower() in line.lower(): print major.lower()