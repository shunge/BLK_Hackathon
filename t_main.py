import pdf2txt
import parse
import sys
import sqliteOperation
import glob

csvPath = "parsedResume.csv"


def writeToCSV(list):
    import csv

    with open(csvPath, 'w') as csvfile:
        fieldnames = ['id', 'filePath', 'fullText']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obj in list:
            path = obj.getPATH()[:-4]
            text = open(obj.getPATH(), 'r').read()
            writer.writerow({'id': obj.getID(), 'filePath': path, 'fullText': text})



def helper(argv):
    orig_stdout = sys.stdout
    sys.stdout = open(argv[1] + '.txt', 'w')
    worker = pdf2txt.TypeConvert()
    worker.parse(argv)
    sys.stdout.close()
    sys.stdout = orig_stdout

    fileName = argv[1] + '.txt'
    return parse.TxtParser.parseFile(fileName)

if __name__ == '__main__':

    list = []
    for filename in glob.glob('samples/*.pdf'):
        list.append(helper(["pdf2txt.py", filename]))

    writeToCSV(list)
    sql = sqliteOperation.sqliteTable()
    sql.createTable()
    sql.insertValue(list)
    sql.lookUp()
