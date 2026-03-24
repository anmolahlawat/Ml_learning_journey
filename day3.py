import pandas as pd

data = {
    "name": ["A","B","C","D"],
    "marks": [90,60,80,50]
}

df = pd.DataFrame(data)




# Task 1

#  Filter marks > 70

print(df[df["marks"]> 70])




# ✅ Task 2

#  Add column:

# "grade" = "Pass" if marks > 60 else "Fail"

df["grade"] = df["marks"].apply(lambda x: "Pass" if x > 60 else "Fail")
print(df)