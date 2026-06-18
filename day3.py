import numpy as np
import pandas as pd

print("===== NUMPY OPERATIONS =====")  

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

print("First 3 Elements:", arr[:3])
print("Last 2 Elements:", arr[-2:])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nMatrix:")
print(matrix)

print("\nFirst 2 Rows:")
print(matrix[:2])

print("\nSecond Column:")
print(matrix[:, 1])

print("\nArray + 10:")
print(arr + 10)

print("\nArray * 2:")
print(arr * 2)

print("\nSquare:")
print(np.square(arr))

print("\nSquare Root:")
print(np.sqrt(arr))

print("\nMean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

print("\nReshaped Array:")
new_arr = np.arange(1, 13)
print(new_arr.reshape(3, 4))


print("\n PANDAS OPERATIONS ")

df = pd.read_csv("student.csv")

print("\nDataset:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDescribe:")
print(df.describe())

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nCSE Students:")
print(df[df["Department"] == "CSE"])

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

print("\nDepartment Statistics:")
print(df.groupby("Department")["Marks"].agg(["mean", "max", "min", "count"]))

print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

print("\nHighest Scorer:")
print(df.loc[df["Marks"].idxmax()])

print("\nLowest Scorer:")
print(df.loc[df["Marks"].idxmin()])