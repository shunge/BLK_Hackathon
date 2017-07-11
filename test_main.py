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

    fileName = argv[1]
    parse.TxtParser.parseFile(fileName)




if __name__ == '__main__':
    main(["pdf2txt.py","samples/sample-resumes_scs_2.pdf"])


