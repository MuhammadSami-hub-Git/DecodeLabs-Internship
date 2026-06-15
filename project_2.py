# Project 2: Data Classification Using AI
# DecodeLabs AI Internship

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#Load the Dataset
iris = load_iris()

X = iris.data      # Features
y = iris.target    # Labels

print("=== Dataset Information ===")
print("Total Samples:", len(X))
print("Total Features:", len(X[0]))

# : Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n=== Data Split ===")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

model = DecisionTreeClassifier()


model.fit(X_train, y_train)

print("\nModel Training Completed!")


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("\n=== Model Evaluation ===")
print("Accuracy: {:.2f}%".format(accuracy * 100))

sample_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample_flower)

print("\n=== New Prediction ===")
print("Predicted Flower Class:", iris.target_names[prediction[0]])