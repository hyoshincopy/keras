from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

train_data = pd.read_csv("./number.csv")
test_data = pd.read_csv("./number_test.csv")


y = train_data["BMI"]

features = ["gender", "height", "weight"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame(
    {'name': test_data.NAME, 'BMI': predictions})
output.to_csv('bmi.csv', index=False)
print("Your submission was successfully saved!")
