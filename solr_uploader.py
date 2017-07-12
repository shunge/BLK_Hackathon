import solr
import csv
import re

# create a connection to a solr server
s = solr.Solr('http://localhost:8983/solr/resume_core')

with open('parsedResume.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     first = True
     for row in spamreader:
         if first:
             first = False
             continue
         id = int(row[0])
         s.delete(id)
         pdf_path = "static/" + row[1]
         pdf_path = str(pdf_path)
         text_path = row[1] + ".txt"
         text_file = open(text_path, 'r')
         text = text_file.read().decode('utf-8', 'ignore')
         text = re.sub(r'\W+', ' ', text)
         # print(id)
         # print(pdf_path)
         # print(text_path)
         doc = dict(
             id=id,
             pdf_path=pdf_path,
             resume_text=text,
         )
         s.add(doc, commit=True)









