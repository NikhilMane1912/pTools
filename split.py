import pandas as pd
import numpy as np

df=pd.read_excel("openClickCombined.xlsx", sheet_name="Sheet1")

GROUP_LENGTH = 2500 # set nr of rows to slice df
j=0

with pd.ExcelWriter('output.xlsx') as writer:
  for i in range(0, len(df), GROUP_LENGTH):
      df[i : i+GROUP_LENGTH].to_excel(writer, sheet_name='{}'.format(j), index=False, header=True)
      j=j+1

# with pd.ExcelWriter('output.xlsx') as writer:
#   for i in range(0, len(df), GROUP_LENGTH):
#       df[i : i+GROUP_LENGTH].to_excel(writer, sheet_name='Row {}'.format(i), index=False, header=True)