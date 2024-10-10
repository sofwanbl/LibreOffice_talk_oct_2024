import pandas as pd
path = "c:/Users/SOFWAN/OneDrive - UNIVERSITAS INDONESIA/Documents/Pembicara/Example - Conditions.ods"
dfnya=pd.read_excel(path, sheet_name="Sheet2")
x=dfnya["Number"].tolist()
for i in range(6):
  if x[i]>1:
    print(x[i],"Positive")
  elif x[i]<1:
    print(x[i],"Negative")
  else:
    print(x[i],"Zero")