import pandas as pd
import numpy as np
import xlsxwriter

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

count_row1=df1.shape[0]
count_row2=df2.shape[0]
count_row3=df3.shape[0]
count_row4=df4.shape[0]
count_row5=df5.shape[0]
count_row6=df6.shape[0]
count_row7=df7.shape[0]
count_row8=df8.shape[0]
count_row9=df9.shape[0]
count_row10=df10.shape[0]
count_row11=df11.shape[0]
count_row12=df12.shape[0]
count_row13=df13.shape[0]
count_row14=df14.shape[0]
count_row15=df15.shape[0]
count_row16=df16.shape[0]
count_row17=df17.shape[0]
count_row18=df18.shape[0]
count_row19=df19.shape[0]
count_row20=df20.shape[0]

print(count_row1)
print(count_row2)
print(count_row3)
print(count_row4)
print(count_row5)
print(count_row6)
print(count_row7)
print(count_row8)
print(count_row9)
print(count_row10)
print(count_row11)
print(count_row12)
print(count_row13)
print(count_row14)
print(count_row15)
print(count_row16)
print(count_row17)
print(count_row18)
print(count_row19)
print(count_row20)
