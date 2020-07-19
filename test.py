# import tensorflow as tf
import numpy as np
import pandas as pd

training_set = pd.read_csv("./number.csv")
testing_set = pd.read_csv("./number_test.csv")

# ? 전체 column중에 학습에 필요 없는열을 drop함수를 통해 지운다
x_train = training_set.drop(['NAME', 'BMI'], axis=1)
y_train = training_set['BMI']
x_test = testing_set.drop(['NAME'], axis=1)
# ? df.fillna 는 결손값을 임의로 넣어주는 함수이다.
x_train['age'] = x_train['age'].fillna(x_train['age'].mean())
x_test['age'] = x_test['age'].fillna(x_test['age'].mean())

# ? 나이를 그룹화 하여 반환한다.


def simplify_ages(df):
    bins = (0, 10, 20, 30, 40, 50)
    group_names = ['Baby', 'Teenager', 'Young Adult', 'Adult', 'Senior']
    categories = pd.cut(df['age'], bins, labels=group_names)
    df['age'] = categories.cat.codes
    return df


tmp = simplify_ages(x_train)

print(tmp)
