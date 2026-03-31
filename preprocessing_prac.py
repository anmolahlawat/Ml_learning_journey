import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [20, None, 25, 30, None],
    'Salary': [20000, 50000, None, 40000, 100000],
    'City': ['Delhi', 'Mumbai', None, 'Chennai', 'Delhi']
}

df = pd.DataFrame(data)


df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['City'].fillna(df['City'].mode()[0], inplace=True)


df = pd.get_dummies(df, columns=['City'])


scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)