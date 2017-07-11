import pdf2txt
import sys

def main():
    worker = pdf2txt.TypeConvert()
    worker.parse(["pdf2txt.py","samples/sample-resumes_scs_2.pdf"])



if __name__ == '__main__':
    sys.exit(main())


