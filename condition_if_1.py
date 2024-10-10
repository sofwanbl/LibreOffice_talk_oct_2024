import pandas as pd
path = "c:/Users/SOFWAN/OneDrive - UNIVERSITAS INDONESIA/Documents/Pembicara/Example - Conditions.ods"
dfnya=pd.read_excel(path, sheet_name="Sheet2")
x=dfnya["Number_py"].tolist()
for i in range(6):
  if x[i]==1:
    print(x[i],"One")
  else:
    print(x[i],"Not One")