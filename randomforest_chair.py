from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

train_data = pd.read_csv("./bcde.csv")
test_data = pd.read_csv("./a_120.csv")

features = []

for i in range(len(train_data.columns)):
    features.append(train_data.columns[i])

features.remove("posture")
# * 확인용 print(features[len(features)-1])

y = train_data["posture"]

# //features = ["gender", "height", "weight"]
# X = pd.get_dummies(train_data[features])
X = pd.get_dummies(train_data)


print(X)
# X_test = pd.get_dummies(test_data[features])
X_test = pd.get_dummies(test_data)

model = RandomForestClassifier(
    n_estimators=100, max_depth=5, random_state=1, max_features=10)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame(
    {'Posture': predictions})
output.to_csv('chair_communication_random_forest.csv', index=False)
print("Your submission was successfully saved!")
print("thats right")
