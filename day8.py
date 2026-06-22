from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

dt_model = DecisionTreeClassifier(random_state=42)

dt_model.fit(X_train, y_train)

dt_predictions = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_predictions)

plt.figure(figsize=(20,10))

plot_tree(
    dt_model,
    filled=True,
    feature_names=data.feature_names,
    class_names=data.target_names,
    rounded=True
)

plt.title("Decision Tree Visualization")
plt.show()

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_predictions)

print("=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

print(f"Decision Tree Accuracy : {dt_accuracy:.4f}")
print(f"Random Forest Accuracy : {rf_accuracy:.4f}")

if rf_accuracy > dt_accuracy:
    print("\nRandom Forest performed better.")
elif rf_accuracy < dt_accuracy:
    print("\nDecision Tree performed better.")
else:
    print("\nBoth models performed equally.")