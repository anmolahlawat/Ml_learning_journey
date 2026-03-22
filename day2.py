"""1. What is Pandas?

👉 Pandas = tool to work with data (tables)

Name   Marks
A      90
B      80

"""



# create dataframe

import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "marks": [90, 80, 85]
}


df = pd.DataFrame(data)
print(df)
print()
# acess colums
print(df["marks"])


# acess row 
print(df.loc[0])
print(df.loc[1])


# filter data
print(df["marks"]>80)


print(df.head(2))


