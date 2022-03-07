import pandas as pd
import numpy as np

df1=pd.read_excel("excel 1.xlsx", sheet_name="Sheet1")
df2=pd.read_excel("excel 2.xlsx", sheet_name="Sheet1")

dfnew = pd.concat([df1,df2]).drop_duplicates(subset=["Email"], keep=False)

file_name = 'subtracted.xlsx'
dfnew.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')