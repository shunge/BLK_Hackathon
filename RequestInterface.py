# importing the requests library
import requests
import json

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