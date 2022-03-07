import pandas as pd

df=pd.read_excel("2019-2022.xlsx", sheet_name="Sheet1")

df = df.loc[(df['Institute'].isin(df['Institute2'].unique()))]

file_name = 'deducted.xlsx'
df.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')