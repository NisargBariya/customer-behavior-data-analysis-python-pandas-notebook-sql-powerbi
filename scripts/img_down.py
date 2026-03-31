import pandas as pd  
import numpy as np
import dataframe_image as dt_i
df = pd.read_csv("D:/pythons/Customer-Trends-Analysis-Project/data/customer_shopping_behavior.csv")
# df = pd.DataFrame(df)
df.head()
dt_i.export(df.describe(include='all'),"Customer-Trends-Analysis-Project/outputs/tabels/tabel_info.png",table_conversion='playwright')
