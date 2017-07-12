# importing the requests library
import requests
import json
import csv
import re
import string

class NLPParser:
    GOOGLEENDPOINT = \
        "https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyAofEz7JEguPw8PGMwKeleaJt4XEVmjkmQ"

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
#SearchEntity(GetEntityResult(ReadTextFiles("samples/output.txt")),"PERSON")

class PersonalInfoExtracter:
    def __init__(self):
        self.All_Majors = []
        self.All_Schools = []
        with open("majors.txt") as f_obj:
            for line in f_obj:
                self.All_Majors.append(line.rstrip())
        with open("Uni.txt") as f_obj:
            for line in f_obj:
                self.All_Schools.append(line.rstrip())


    def Major_Extraction(self, path):
        for major in self.All_Majors:
            major_lower = major.lower()
            searchfile = open(path, "r")
            for line in searchfile:
                Searchable_line = line.lower().replace("-", " ")
                if major_lower in Searchable_line:
                    if re.search('(masters|bachelor|b.s.|bs|major|phd|ms)', Searchable_line) is not None:
                        print major_lower
                        return major_lower

    def School_Extraction(self, path):
        for school in self.All_Schools:
            school_lower = school.lower()
            searchfile = open(path, "r")
            for line in searchfile:
                Searchable_line = line.lower()
                if school_lower in Searchable_line:
                        print school_lower
                        return school_lower

if __name__ == '__main__':
    # parser = NLPParser()
    # parser.ReadTextFiles("samples/output.txt")
    # parser.GetEntityResult()
    # parser.SearchEntity("PERSON")

    extracter = PersonalInfoExtracter()
    extracter.Major_Extraction("samples/output_11.txt")
    # parser.nltkNER()