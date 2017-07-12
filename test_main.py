import pdf2txt
import parse
import sys
import sqliteOperation



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

    # list = []
    # for i in range (1, 14):
    #     path = "samples/sample-resumes_scs_%d.pdf" % i
    #     list.append(helper(["pdf2txt.py", path]))
    #
    # for i in range(1, 3):
    #     path = "samples/sample-resumes_finance_%d.pdf" % i
    #     list.append(helper(["pdf2txt.py", path]))

    sql = sqliteOperation.sqliteTable()
    # sql.createTable()
    # sql.insertValue(list)
    sql.lookUp()

#     for i in range (1, 5):
#         path = "samples/sample-resumes_finance_%d.pdf" % i
#         main(["pdf2txt.py", path])

