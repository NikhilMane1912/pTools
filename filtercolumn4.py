import os
import pandas as pd
import numpy as np

cwd = os.path.abspath('') 
files = os.listdir(cwd)

clientName = "RoyalCyber"
yearsOfExperience = "1Plus"
position = "CloudEngineer"

fromYear = 2019
# toYear = 2014
# toYear = 'above'
toYear = 'below'

df = pd.DataFrame()
_jdir = cwd + '\\Gen\\'

x = []

for file in files:
    if file.endswith('.xlsx'):
        temp_df = pd.read_excel(file, sheet_name='result')
        # temp_df['Graduation_Year'] = pd.to_numeric(temp_df['Graduation_Year'], errors='coerce').astype('Int64')
        temp_df['Graduation_Year'] = np.floor(pd.to_numeric(temp_df['Graduation_Year'], errors='coerce')).astype('Int64')
        temp_df = temp_df.dropna(subset = ['Graduation_Year'])
        temp_df = temp_df.drop_duplicates(subset=["Email"], keep="first")

        if (type(fromYear) == int and type(toYear) == int):
            if fromYear < toYear:
                fromYear, toYear = fromYear, toYear
                temp_df = temp_df.loc[(temp_df['Graduation_Year'] >= fromYear) & (temp_df['Graduation_Year'] <= toYear)]
            elif fromYear > toYear:
                fromYear, toYear = toYear, fromYear
                temp_df = temp_df.loc[(temp_df['Graduation_Year'] >= fromYear) & (temp_df['Graduation_Year'] <= toYear)]
            elif fromYear == toYear:
                temp_df = temp_df.loc[(temp_df['Graduation_Year'] == fromYear) & (temp_df['Graduation_Year'] == toYear)]
        elif (type(fromYear) == int and type(toYear) == str):
            if toYear == 'above':
                temp_df = temp_df.loc[(temp_df['Graduation_Year'] >= fromYear)]
            elif toYear == 'below':
                temp_df = temp_df.loc[(temp_df['Graduation_Year'] <= fromYear)]

        temp_df = temp_df.sort_values('Graduation_Year')

        filename = os.path.splitext(file)[0]
        filenameToBeGen = filename + ' ' + clientName + yearsOfExperience + position
        filenameToBeGenWithExt =  filenameToBeGen + '.xlsx'
        if not os.path.exists(_jdir):
            os.makedirs(_jdir)

        temp_df.to_excel(cwd + '\\Gen\\' + filenameToBeGenWithExt, index=False)

        count_row=temp_df.shape[0]
        # print(filename,'\t',count_row)
        print("{0}\t{1}".format(filenameToBeGen, count_row))

        x.append([filenameToBeGen, count_row])

        df = df.append(pd.read_excel(cwd + '\\Gen\\' + filenameToBeGenWithExt), ignore_index=False)
        df = df.drop_duplicates(subset=["Email"], keep="first")
        df = df.sort_values('Graduation_Year')

        df.head() 
        df.to_excel(cwd + '\\Gen\\' + clientName + yearsOfExperience + position + '.xlsx', index=False)

count_df = pd.DataFrame(x)
print(count_df)
count_df.to_excel(cwd + "\\Gen\\" + clientName + yearsOfExperience + position + 'count.xlsx', index=False)