# data preprocessing and feature engineering

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [20, None, 25, 30],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai']
}

df = pd.DataFrame(data)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Encoding
df = pd.get_dummies(df, columns=['City'])

# Scaling
scaler = StandardScaler()
df[['Age']] = scaler.fit_transform(df[['Age']])

print(df)