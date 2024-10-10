import pandas as pd
path = "c:/Users/SOFWAN/OneDrive - UNIVERSITAS INDONESIA/Documents/Pembicara/Example - Conditions.ods"
dfnya=pd.read_excel(path, sheet_name="Sheet2")
x=dfnya["Number"].tolist()
for i in range(6):
  if x[i]>=1 and x[i]<10:
    print(x[i],"Group A")
  elif x[i]>=10 and x[i]<20:
    print(x[i],"Group B")
  elif x[i]>=20 and x[i]<30:
    print(x[i],"Group C")
  else:
    print(x[i],"Group D")