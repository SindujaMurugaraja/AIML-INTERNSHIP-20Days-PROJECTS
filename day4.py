import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print(" STUDENT DATASET ")
print(df)

df["Total"] = df["Maths"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3

print("\n DATASET WITH TOTAL & AVERAGE ")
print(df)

top_student = df.loc[df["Total"].idxmax()]

print("\n TOP PERFORMER ")
print(top_student)

print("\n SUBJECT-WISE AVERAGES ")
subject_avg = df[["Maths", "Science", "English"]].mean()
print(subject_avg)

print("\n DESCRIBE ")
print(df.describe())

plt.figure(figsize=(6,4))
subject_avg.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Total"])
plt.title("Total Marks of Students")
plt.ylabel("Total Marks")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
plt.pie(
    df["Average"],
    labels=df["Name"],
    autopct="%1.1f%%"
)
plt.title("Average Marks Distribution")
plt.show()

print("\n INSIGHTS ")
print("Top Performer :", top_student["Name"])
print("Highest Total Marks :", top_student["Total"])
print("Best Subject :", subject_avg.idxmax())
print("Average Marks Across Subjects:")
print(subject_avg)