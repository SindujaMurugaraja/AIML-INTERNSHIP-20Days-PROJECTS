import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("housing.csv")

print("Dataset")
print(df)

X = df[["Area", "Bedrooms"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Coefficients")
print("Area Coefficient:", model.coef_[0])
print("Bedrooms Coefficient:", model.coef_[1])
print("Intercept:", model.intercept_)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)

sample = [[2400, 4]]
prediction = model.predict(sample)

print("\nPredicted House Price:", prediction[0])
