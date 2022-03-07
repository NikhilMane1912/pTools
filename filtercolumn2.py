import pandas as pd
import numpy as np

df1 = pd.read_excel("python chunk no 5.xlsx", sheet_name='result')

df = pd.concat([df1], ignore_index=True)

# df['Graduation_Year'] = pd.to_numeric(df['Graduation_Year'], downcast='integer', errors='coerce')

df['Graduation_Year'] = pd.to_numeric(df['Graduation_Year'], errors='coerce').astype('Int64')
df = df.dropna(subset = ['Graduation_Year'])

dfnew = df.drop_duplicates(subset=["Email"], keep="first")

dfnew = dfnew.loc[(dfnew['Graduation_Year'] >= 2017) & (dfnew['Graduation_Year'] <= 2019)]
# dfnew = dfnew.loc[(dfnew['Graduation_Year'] <= 2015)]

dfnew = dfnew.sort_values('Graduation_Year')

file_name = 'python 5 yellow class 1-3 devops.xlsx'
dfnew.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')