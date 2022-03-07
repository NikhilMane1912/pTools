import pandas as pd

df=pd.read_excel("1-(2+3).xlsx", sheet_name="Sheet1")

df = df.loc[~(df['user__email'].isin(df['email'].unique()))]

file_name = 'deducted.xlsx'
df.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')