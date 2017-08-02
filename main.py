import os
from PyPDF2 import PdfFileWriter, PdfFileReader
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(BASE_DIR, 'files')


def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]


def merge_pdf(files_name):
    output = PdfFileWriter()
    for name in files_name:
        append_pdf(PdfFileReader(open('{0}/{1}'.format(FILE_DIR, name), 'rb')), output)
    output.write(open('{0}/{1}'.format(FILE_DIR, 'teste.pdf'), 'wb'))

if __name__ == "__main__":
    files = os.listdir(FILE_DIR)
    merge_pdf(files)
