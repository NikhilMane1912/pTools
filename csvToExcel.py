import os
import pandas as pd
import numpy as np

cwd = os.path.abspath('') 
files = os.listdir(cwd)

# clientName = "combinedData"
# yearsOfExperience = "All"
# position = "Profile"

# fromYear = 2019
# toYear = 2014
# toYear = 'above'
# toYear = 'below'

df = pd.DataFrame()
_jdir = cwd + '\\Gen\\'

x = []

i = 1

for file in files:
    if file.endswith('.csv'):
        df_new = pd.read_csv(file)
        # df_new = pd.read_csv(file,error_bad_lines=False)
        # df_new = pd.read_csv(file,sep='\t',lineterminator='\r')
        filename = os.path.splitext(file)[0]
        filenameToBeGen = filename
        filenameToBeGenWithExt =  filenameToBeGen + '.xlsx'
        if not os.path.exists(_jdir):
            os.makedirs(_jdir)

        CSVtoExcel = pd.ExcelWriter(cwd + '\\Gen\\' + filenameToBeGenWithExt)
        df_new.to_excel(CSVtoExcel, index = False)
        CSVtoExcel.save()
        print(i,"\t",filenameToBeGenWithExt)
        i = i+1
