import numpy as np
import pandas as pd

# -----------------------------
# 1. Load Dataset
# -----------------------------

df = pd.read_csv("student_scores.csv")

print("Dataset Loaded")
print(df.head())

# Convert scores to NumPy array
scores = df.iloc[:, 1:].values

print("\nNumPy Array Shape:")
print(scores.shape)

# -----------------------------
# 2. Creating Arrays
# -----------------------------

a = np.array([1,2,3,4,5])
print("\n1D Array:", a)

b = np.array([[1,2,3],[4,5,6]])
print("\n2D Array:\n", b)

# -----------------------------
# 3. Array Properties
# -----------------------------

print("\nShape:", scores.shape)
print("Dimensions:", scores.ndim)
print("Data Type:", scores.dtype)
print("Size:", scores.size)

# -----------------------------
# 4. Indexing
# -----------------------------

print("\nFirst Student Scores:")
print(scores[0])

print("\nMath Score of First Student:")
print(scores[0,0])

# -----------------------------
# 5. Slicing
# -----------------------------

print("\nFirst 5 Students:")
print(scores[:5])

print("\nMath Scores of First 10 Students:")
print(scores[:10,0])

# -----------------------------
# 6. Boolean Filtering
# -----------------------------

high_math = scores[:,0] > 90
print("\nStudents with Math > 90")
print(scores[high_math])

# -----------------------------
# 7. Basic Arithmetic
# -----------------------------

print("\nAdd 5 bonus marks")
bonus_scores = scores + 5
print(bonus_scores[:5])

# -----------------------------
# 8. Vectorized Operations
# -----------------------------

total_scores = scores.sum(axis=1)

print("\nTotal Score per Student")
print(total_scores[:10])

average_scores = scores.mean(axis=1)

print("\nAverage Score per Student")
print(average_scores[:10])

# -----------------------------
# 9. Statistics
# -----------------------------

print("\nMean Score per Subject")
print(scores.mean(axis=0))

print("\nMaximum Scores")
print(scores.max(axis=0))

print("\nMinimum Scores")
print(scores.min(axis=0))

print("\nStandard Deviation")
print(scores.std(axis=0))

# -----------------------------
# 10. Reshaping Arrays
# -----------------------------

arr = np.arange(12)

reshaped = arr.reshape(3,4)

print("\nReshaped Array")
print(reshaped)

# -----------------------------
# 11. Stacking Arrays
# -----------------------------

a = np.array([1,2,3])
b = np.array([4,5,6])

print("\nVertical Stack")
print(np.vstack((a,b)))

print("\nHorizontal Stack")
print(np.hstack((a,b)))

# -----------------------------
# 12. Matrix Operations
# -----------------------------

matrix_a = np.array([[1,2],[3,4]])
matrix_b = np.array([[5,6],[7,8]])

print("\nMatrix Multiplication")
print(np.dot(matrix_a, matrix_b))

# -----------------------------
# 13. Random Number Generation
# -----------------------------

print("\nRandom Numbers")
print(np.random.rand(3,3))

print("\nRandom Integers")
print(np.random.randint(1,100,10))

# -----------------------------
# 14. Sorting
# -----------------------------

sorted_scores = np.sort(scores[:,0])

print("\nSorted Math Scores")
print(sorted_scores)

# -----------------------------
# 15. Finding Indices
# -----------------------------

top_students = np.where(scores[:,0] > 90)

print("\nIndices where Math > 90")
print(top_students)

# -----------------------------
# 16. Broadcasting
# -----------------------------

weights = np.array([0.2,0.2,0.2,0.2,0.2])

weighted_scores = scores * weights

print("\nWeighted Scores")
print(weighted_scores[:5])