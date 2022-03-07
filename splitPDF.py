from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
import os

cwd = os.path.abspath('')
files = os.listdir(cwd)
_dir = cwd

# df = pd.read_excel('COP.xlsx', sheet_name='Certificates')
# ranklist = df['Rank'].tolist()
# mylist = df['Name'].tolist()

for file in files:
    if file.endswith('.pdf'):
        inputpdf = PdfFileReader(open(file, "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    # k = str(ranklist[i])
    # j = mylist[i]
    _jdir = os.path.join(_dir + "\\Gen\\")
    if not os.path.exists(_jdir):
        os.makedirs(_jdir)

    outputFilename = os.path.join(_jdir, "%s.pdf" % i)

    with open(outputFilename, "wb") as outputStream:
        output.write(outputStream)