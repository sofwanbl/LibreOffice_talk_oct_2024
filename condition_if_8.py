import pandas as pd

path = "c:/Users/SOFWAN/OneDrive - UNIVERSITAS INDONESIA/Documents/Pembicara/Example - Conditions.ods"
dfnya = pd.read_excel(path, sheet_name="Sheet2")
x = dfnya["Number"].tolist()

# Print the numbers
for i in range(6):
    print(x[i])

countx=0
# Print result
for i in range(6):
    if x[i] >= 0 and x[i]<=10:
        countx = countx + 1
print("Result : ", countx)