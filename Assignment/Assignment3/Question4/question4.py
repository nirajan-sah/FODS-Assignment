'''
Import the data form IPL_Data and displays it in tabular format
It is done by using python library pandas
'''

import pandas as pd

#data_frame to read csv file using pandas
df = pd.read_csv("IPL_Data.csv")

print(df)