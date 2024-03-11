import pandas as pd

excel_file = "datos.xlsx"

df = pd.read_excel(excel_file)

print(df.head())
