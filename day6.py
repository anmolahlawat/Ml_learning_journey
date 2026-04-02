# logistic regression 

#  1. What is Logistic Regression?

# 👉 Used when output is categorical

# Examples:
# 	•	Spam / Not Spam
# 	•	Pass / Fail
# 	•	Disease / No Disease


# Core Function (Sigmoid)
# sigmoid  = 1/1+e^-x


#  How it Works (Simple Flow)
# 	1.	Take input (x)
# 	2.	Apply linear equation (z = mx + b)
# 	3.	Pass through sigmoid
# 	4.	Get probability
# 	5.	Convert to class




from sklearn.linear_model import LogisticRegression
import numpy as np

# Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1])

# Model
model = LogisticRegression()
model.fit(X, y)

# Prediction
print(model.predict([[3]]))
print(model.predict([[5]]))