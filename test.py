# import tensorflow as tf
import numpy as np
import pandas as pd
import keras
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

# ? 키를 그룹화 하여 반환한다


def simplify_height(df):
    bins = (0, 160, 175, 185, 200)
    group_names = ['Short', 'Standard', 'Long', 'Very Long']
    categories = pd.cut(df['height'], bins, labels=group_names)
    df['height'] = categories.cat.codes
    return df

# ? 몸무게를 그룹화 하여 반환한다


def simplify_weight(df):
    bins = (0, 50, 70, 90, 140)
    group_names = ['Light', 'Standard', 'Heavy', 'Very Heavy']
    categories = pd.cut(df['weight'], bins, labels=group_names)
    df['weight'] = categories.cat.codes
    return df
# ? 성별은 그룹화 할 필요 없어보이지만, 성별은 str 자료형이므로 이산데이터로 변경해야 한다


def simplify_gender(df):
    df['gender'] = pd.Categorical(df['gender'])
    df['gender'] = df['gender'].cat.codes
    return df


def transform_features(df):
    df = simplify_ages(df)
    df = simplify_gender(df)
    df = simplify_height(df)
    df = simplify_weight(df)
    return df


#! simplify_ 함수를 통해서 크고 복잡한 값들을 작은 값으로 대체한다

print(transform_features(x_train))
print(transform_features(x_test))
