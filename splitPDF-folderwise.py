from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
import os

_dir = "E:\CGP\Generated Certificates"

df = pd.read_excel('COP.xlsx', sheet_name='Certificates')
ranklist = df['Rank'].tolist()
mylist = df['Name'].tolist()

inputpdf = PdfFileReader(open("COP.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    k = str(int(ranklist[i]))
    j = mylist[i]
    _jdir = os.path.join(_dir, "%s %s" %(k,j))
    if not os.path.exists(_jdir):
        os.makedirs(_jdir)

    outputFilename = os.path.join(_jdir, "%s.pdf" % j)

    with open(outputFilename, "wb") as outputStream:
        output.write(outputStream)