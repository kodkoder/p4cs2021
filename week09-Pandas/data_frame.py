import pandas as pd
listDAta= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
#print(df.head(4))

path = "./data/"
#csvFilename = path + 'grades.csv'
#df.to_csv(csvFilename)
excelFilename = path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

print(df.describe())
print(type(df.describe()))

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")

mean = df.describe().loc['mean','grade']
print(mean)
# or
mean = df['grade'].mean()
print (mean)