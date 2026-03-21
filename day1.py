""" Machine learning = machine learns from data instead of hard coding rules"""

# ✅ 1. Supervised Learning

# 👉 Data has input + output

# Example:
# 	•	Marks → Grade
# 	•	House → Price




"""
2. Unsupervised Learning

👉 Only input, no output

Example:
	•	Group similar people"""



"""
3. Reinforcement Learning

👉 Learn by reward/penalty

Example:
	•	Games"""







import numpy as np

arr = np.array([1,2,3,4])
print(arr)
print(arr*2)

print(type(arr))





# ✅ Task 1
# 👉 Convert to NumPy array
# 👉 Multiply by 3

ar = [5,10,15]
ar = np.array(ar)
print(ar)


# add 10 to each element 
ar1 = [2,4,6]
ar1 = np.array(ar1)
print(ar1+10)



#  1. Indexing (Access elements)


import numpy as np

ar2 = np.array([10,20,30,40])

print(ar2[0])   
print(ar2[2])   

print(ar2[::-1])
print(ar2[::])
print(ar2[1:4])
print(ar2[2:3])


# 2d array
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr1)
print(arr1[0][1])
print(arr1[1][1])
print(arr1[1][2])
print(arr1[1][3])
print(arr1[0][3])
print(arr1[1][0])



print()
print(arr1.shape)
print(arr1.sum())
print(arr1.mean())
