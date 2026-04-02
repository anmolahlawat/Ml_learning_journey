import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Data
data = {
    "Experience": [1,2,3,4,5,6,7,8],
    "Salary": [18000,28000,38000,50000,62000,75000,88000,100000]
}

df = pd.DataFrame(data)

# Features & Target
x = df[["Experience"]]
y = df["Salary"]

# Split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

# Model
model = LinearRegression()
model.fit(x_train, y_train)

# Prediction
y_pred = model.predict(x_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# Plot
plt.scatter(x, y, label="Actual Data")
plt.plot(x, model.predict(x), color='red', label="Best Fit Line")
plt.legend()
plt.show()