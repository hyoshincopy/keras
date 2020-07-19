# import tensorflow as tf
import numpy as np
import pandas as pd

training_set = pd.read_csv("./number.csv")
testing_set = pd.read_csv("./number_test.csv")

# ? 전체 column중에 학습에 필요 없는열을 drop함수를 통해 지운다
x_train = training_set.drop(['NAME', 'BMI'], axis=1)
y_train = training_set['BMI']
x_test = testing_set.drop(['NAME'], axis=1)

x_train['age'] = x_train['age'].fillna(x_train['age'].mean())
x_test['age'] = x_test['age'].fillna(x_test['age'].mean())
