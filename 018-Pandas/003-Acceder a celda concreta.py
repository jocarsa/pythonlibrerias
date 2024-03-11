# pip install pandas
# pip install openpyxl

import pandas as pd

excel_file = "datos.xlsx"

df = pd.read_excel(excel_file)

print(df.head())

celda =  df.iloc[1, 1]
print(celda)
