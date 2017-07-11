import pdf2txt
from RequestInterface import *


def main():
    worker = pdf2txt.ConvertToText("samples/", "samples/")
    worker.parse("sample-resumes_scs_1.pdf", "sample-resumes_scs_1.txt")



if __name__ == '__main__':
    main()


