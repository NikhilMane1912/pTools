import pandas as pd
import numpy as np

df1=pd.read_excel("ansible yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df2=pd.read_excel("aws yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df3=pd.read_excel("cicd yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df4=pd.read_excel("docker yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df5=pd.read_excel("java 1 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df6=pd.read_excel("java 2 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df7=pd.read_excel("java 3 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df8=pd.read_excel("java 4 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df9=pd.read_excel("java 5 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df10=pd.read_excel("java 6 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df11=pd.read_excel("jenkins yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df12=pd.read_excel("kubernetes yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df13=pd.read_excel("nagios yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df14=pd.read_excel("puppet yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df15=pd.read_excel("python 1 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df16=pd.read_excel("python 2 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df17=pd.read_excel("python 3 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df18=pd.read_excel("python 4 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df19=pd.read_excel("python 5 yellow class 1-3 devops.xlsx", sheet_name="Sheet1")
df20=pd.read_excel("security yellow class 1-3 devops.xlsx", sheet_name="Sheet1")

df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20], ignore_index=True)

dfnew = df.drop_duplicates(subset=["Email"], keep="first")
# dfnew = df.loc[df['Job_Seeker'] == 'Y']

file_name = 'combinedDataYellowClassDevops1-3.xlsx'
dfnew.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')