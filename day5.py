#  Linear regression


""" 

It finds a relationship between input (X) and output (y) using a straight line.
Goal = minimize error between actual vs predicted
Equation of linear regression :  Y = Mx + b


Mean Squared Error = 1/n summition(y - ŷ)^2


m and b ar random and changed using gradient descent
m = m - alpha* -2/n summition x(y - ŷ)

b = b - alpha* -2/n summition (y - ŷ)
 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# X = np.array([[1], [2], [3], [4], [5]])
# y = np.array([2, 4, 5, 4, 5])



# model = LinearRegression()

# model.fit(X,y)


# y_predict = model.predict(X)



# plt.scatter(X,y)
# plt.plot(X,y_predict)
# plt.show()






# salary prediction 
data = {
"Experience": [1,2,3,4,5,6,7,8,9,10],
"Salary": [15000,25000,35000,48000,60000,72000,85000,97000,110000,125000]
}

df = pd.DataFrame(data)
print(df.head())


x = df[["Experience"]]
y = df["Salary"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("MSE:", mean_squared_error(y_test, y_pred))

from sklearn.metrics import r2_score
print("R2 Score:", r2_score(y_test, y_pred))

# Plot
plt.scatter(x, y, label="Data")
plt.plot(x, model.predict(x), color='red', label="Best Fit Line")
plt.legend()
plt.show()