import os
import pandas as pd
import numpy as np

cwd = os.path.abspath('') 
files = os.listdir(cwd)

clientName = "combinedData"
yearsOfExperience = "All"
position = "Profile"

# fromYear = 2019
# toYear = 2014
# toYear = 'above'
# toYear = 'below'

df = pd.DataFrame()
_jdir = cwd + '\\Gen\\'

x = []

for file in files:
    if file.endswith('.xlsx'):
        temp_df = pd.read_excel(file, sheet_name='Sheet1')
        # temp_df = temp_df.loc[ : , temp_df.columns != 'Profile Url']
        # temp_df = temp_df.loc[ : , temp_df.columns != 'Resume Url']
        temp_df.drop(['Profile Url', 'Resume Url'], axis=1, errors='ignore')
        temp_df["Email"] = temp_df['Email'].astype(str).str.lower()
        # temp_df.drop(['resume', 'HE_Profile_Link'], axis=1, errors='ignore')
        # temp_df = temp_df[['Name','Email','Theme']]
        # temp_df['Graduation_Year'] = pd.to_numeric(temp_df['Graduation_Year'], errors='coerce').astype('Int64')
        # temp_df = temp_df.dropna(subset = ['Graduation_Year'])
        temp_df = temp_df.drop_duplicates(subset=["Email"], keep="first")

        # if (type(fromYear) == int and type(toYear) == int):
        #     if fromYear < toYear:
        #         fromYear, toYear = fromYear, toYear
        #         temp_df = temp_df.loc[(temp_df['Graduation_Year'] >= fromYear) & (temp_df['Graduation_Year'] <= toYear)]
        #     elif fromYear > toYear:
        #         fromYear, toYear = toYear, fromYear
        #         temp_df = temp_df.loc[(temp_df['Graduation_Year'] >= fromYear) & (temp_df['Graduation_Year'] <= toYear)]
        #     elif fromYear == toYear:
        #         temp_df = temp_df.loc[(temp_df['Graduation_Year'] == fromYear) & (temp_df['Graduation_Year'] == toYear)]
        # elif (type(fromYear) == int and type(toYear) == str):
        #     if toYear == 'above':
        #         temp_df = temp_df.loc[(temp_df['Graduation_Year'] >= fromYear)]
        #     elif toYear == 'below':
        #         temp_df = temp_df.loc[(temp_df['Graduation_Year'] <= fromYear)]

        # temp_df = temp_df.sort_values('Graduation_Year')

        filename = os.path.splitext(file)[0]
        filenameToBeGen = filename + ' ' + clientName + yearsOfExperience + position
        filenameToBeGenWithExt =  filenameToBeGen + '.xlsx'
        if not os.path.exists(_jdir):
            os.makedirs(_jdir)

        # temp_df.to_excel(cwd + '\\Gen\\' + filenameToBeGenWithExt, index=False)

        count_row=temp_df.shape[0]
        # print(filename,'\t',count_row)
        print("{0}\t{1}".format(filenameToBeGen, count_row))

        x.append([filenameToBeGen, count_row])

        df = df.append(temp_df, ignore_index=False)
        df = df.drop_duplicates(subset=["Email"], keep="first")
        # df = df.sort_values('Graduation_Year')

        df.head() 
        df.to_excel(cwd + '\\Gen\\' + clientName + yearsOfExperience + position + '.xlsx', index=False)

GROUP_LENGTH = 50000 # set nr of rows to slice df
j=0

with pd.ExcelWriter(cwd + '\\Gen\\' + 'output.xlsx') as writer:
    for i in range(0, len(df), GROUP_LENGTH):
        df[i : i+GROUP_LENGTH].to_excel(writer, sheet_name='{}'.format(j), index=False, header=True)
        j=j+1

count_df = pd.DataFrame(x)
print(count_df)
# count_df.to_excel(cwd + "\\Gen\\" + clientName + yearsOfExperience + position + 'count.xlsx', index=False)