import pandas as pd
import numpy as np

filename = "jitter"

df=pd.read_excel(filename+".xlsx", sheet_name="Sheet1")

GROUP_LENGTH = 23032 # set nr of rows to slice df
j=0

with pd.ExcelWriter('output.xlsx') as writer:
  for i in range(0, len(df), GROUP_LENGTH):
      t_df = df[i : i+GROUP_LENGTH]
      t_df[["Email"]].to_csv(filename + " " + str(j) +'.csv', index=False)
      t_df[["Email"]].to_excel(writer, sheet_name='{}'.format(j), index=False, header=True)
      # t_df["Email"].to_csv(filename + " " + str(j) +'.csv', index=False)
      # t_df["Email"].to_excel(writer, sheet_name='{}'.format(j), index=False, header=True)
      j=j+1

# with pd.ExcelWriter('output.xlsx') as writer:
#   for i in range(0, len(df), GROUP_LENGTH):
#       df[i : i+GROUP_LENGTH].to_excel(writer, sheet_name='Row {}'.format(i), index=False, header=True)