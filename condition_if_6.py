import pandas as pd

path = "c:/Users/SOFWAN/OneDrive - UNIVERSITAS INDONESIA/Documents/Pembicara/Example - Conditions.ods"
dfnya = pd.read_excel(path, sheet_name="Sheet3")
x = dfnya["Number 1"].tolist()
y = dfnya["Number 2"].tolist()
z = dfnya["Number 3"].tolist()
sumx = 0
print("Number 1 | Number 2 | Number 3")
for i in range(6):
    print(x[i],"|", y[i], "|", z[i])

sumx=0

for i in range(6):
    if x[i] >5 and y[i] > 5:
        sumx = sumx + z[i]
print("Result : ", sumx)
