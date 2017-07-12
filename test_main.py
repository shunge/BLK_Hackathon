import pdf2txt
import parse
import sys

def main(argv):
    orig_stdout = sys.stdout
    sys.stdout = open(argv[1] + '.txt', 'w')
    worker = pdf2txt.TypeConvert()
    worker.parse(argv)
    sys.stdout.close()
    sys.stdout = orig_stdout

    fileName = argv[1] + '.txt'
    parse.TxtParser.parseFile(fileName)

if __name__ == '__main__':
    for i in range (1, 5):
        path = "samples/sample-resumes_finance_%d.pdf" % i
        main(["pdf2txt.py", path])


