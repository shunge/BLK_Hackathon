# importing the requests library
import requests
import json

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
        if entity == entry[u'type']:
            print entry[u'name']
    #print ResultJSON[u'entities']

SearchEntity(GetEntityResult(ReadTextFiles("samples/output.txt")),"PERSON")