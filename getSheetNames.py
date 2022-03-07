import os
import pandas as pd
import numpy as np

cwd = os.path.abspath('') 
files = os.listdir(cwd)

df = pd.DataFrame()

x = []

for file in files:
    if file.endswith('.xlsx'):
        df = pd.read_excel(file, None)
        # if(str(df.keys()) != 'dict_keys([\'result\'])'):
            # print(str(file))
        print(file,"\t",str(df.keys()))