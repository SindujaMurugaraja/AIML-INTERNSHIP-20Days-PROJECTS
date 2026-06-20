import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")

print("Original Dataset")
print(df)


df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter Handling Missing Values")
print(df)

encoder = LabelEncoder()
df["Department"] = encoder.fit_transform(df["Department"])

print("\nAfter Encoding Department")
print(df)

X = df[["Age", "Salary", "Department"]]
y = df["Department"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
X_scaled,
y,
test_size=0.2,
random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))

print("\nData Preprocessing Completed Successfully!")
