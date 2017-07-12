# importing the requests library
import requests
import json
import csv
import re
import string

<<<<<<< HEAD
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

def Major_Extraction(path):
    for major in All_Majors:
        major_lower = major.lower()
        searchfile = open(path, "r")
        for line in searchfile:
            Searchable_line = line.lower().replace("-", " ")
            if major_lower in Searchable_line:
                if re.search('(masters|bachelor|b.s.|bs|major|phd|ms)', Searchable_line) is not None:
                    print major_lower

All_Schools = []
with open("Uni.txt") as f_obj:
    All_Schools = File_Reader(f_obj)

def School_Extraction(path):
    for school in All_Schools:
        school_lower = school.lower()
        searchfile = open(path, "r")
        for line in searchfile:
            Searchable_line = line.lower()
            if school_lower in Searchable_line:
                    print school_lower

Major_Extraction("samples/output_13.txt")
School_Extraction("samples/output_13.txt")
=======
class NLPParser:
    GOOGLEENDPOINT = "https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyAofEz7JEguPw8PGMwKeleaJt4XEVmjkmQ"

    def __init__(self):
        self.data = None
        self.json = None
        self.str = ""
        pass


    def ReadTextFiles(self, fileName):
        with open(fileName, "r") as myfile:
            data = myfile.read()
            self.data = data

    def GetEntityResult(self):
        data = {
          "encodingType": "UTF8",
          "document": {
            "type": "PLAIN_TEXT",
            "content": self.data
          }
        }
        r = requests.post(url = NLPParser.GOOGLEENDPOINT, json=data)
        self.json = json.loads(r.text)

    def SearchEntity(self, entity):
        str = ""
        Result = []
        length = len(self.json[u'entities'])
        for i in range(length):
            entry = self.json[u'entities'][i]
            if entity == entry[u'type']:
                print entry[u'name']
                str += entry[u'name'] + " "
        self.str = str

    def nltkNER(self):
        from nltk import word_tokenize, pos_tag, ne_chunk
        tree = ne_chunk(pos_tag(word_tokenize(self.str)))
        print tree




if __name__ == '__main__':
    parser = NLPParser()
    parser.ReadTextFiles("samples/output.txt")
    parser.GetEntityResult()
    parser.SearchEntity("PERSON")
    # parser.nltkNER()



# SearchEntity(GetEntityResult(ReadTextFiles("samples/output.txt")),"PERSON")
>>>>>>> 6d9b03af6778322d0e142976630bd4a284c776e4
