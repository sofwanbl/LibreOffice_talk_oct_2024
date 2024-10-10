import pandas as pd
path = "c:/Users/SOFWAN/OneDrive - UNIVERSITAS INDONESIA/Documents/Pembicara/Example - Conditions.ods"
dfnya=pd.read_excel(path, sheet_name="Sheet2")
x=dfnya["Number"].tolist()
sumx=0
for i in range(6):
  print(x[i])

for i in range(6):
  if x[i]==5:
    sumx=sumx+x[i]
print("Result : ",sumx)
