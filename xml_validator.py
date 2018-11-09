
import sys
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

def parseFile(fileName):
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(fileName)


if __name__ == '__main__':
    args = sys.argv
    try:
        filename = args[1]
    except Exception:
        print('\tERROR: no input file!')
    try:
        parseFile(filename)
        print('\n\t:), %s is OK!\n' % filename)
    except Exception as e:
        print('\n\t:(,  Error found in file:%s\n' % e)
