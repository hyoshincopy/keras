

# import tensorflow as tf
#! 참조 https://www.kaggle.com/jameskhoo/deep-learning-with-keras-and-tensorflow
import numpy as np
import pandas as pd
import keras
import matplotlib.pyplot as plt
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


print(transform_features(x_train))
transform_features(x_test)

#! simplify_ 함수를 통해서 크고 복잡한 값들을 작은 값으로 대체한다

# model = keras.models.Sequential()
# # ? input_shape 인 입력 형태인데, 전체 columns의 개수는 6개인데
# # ? 그 중 학습 할 column은 NAME과 BMI를 제외한 4가지 이므로 input_shape=(4,) 가 된다
# model.add(keras.layers.Dense(32, activation='relu', input_shape=(4,)))
# model.add(keras.layers.Dense(32, activation='relu'))
# # model.add(keras.layers.Dense(8, activation='relu'))
# model.add(keras.layers.Dense(1, activation='sigmoid'))
# # ? 출처에서는 RMSprop 옵티마이저를 사용했다
# # model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.001),loss=keras.losses.categorical_crossentropy,metrics=keras.metrics.BinaryAccuracy)
# model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=0.001),
#               loss=keras.losses.binary_crossentropy,
#               metrics=[keras.metrics.binary_accuracy]

#               )
# y_train = np.asarray(y_train)
# x_train = np.asarray(x_train)
# x_test = np.asarray(x_test)

# # ? validation_size는 batch_size와 같다.(많은 양의 학습 시 몇 개씩 끊어서 할 것인가?)
# # ? 배치사이즈는 학습데이터가 n개가 있다면 최대 n-1개까지 설정가능하다. 그 이상 설정 시 에러
# validation_size = 5

# x_val = x_train[:validation_size]
# partial_x_train = x_train[validation_size:]

# y_val = y_train[:validation_size]
# partial_y_train = y_train[validation_size:]

# history = model.fit(partial_x_train, partial_y_train,
#                     epochs=30, validation_data=(x_val, y_val))
# acc = history.history['binary_accuracy']
# val_acc = history.history['val_binary_accuracy']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs = range(1, len(acc) + 1)
# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')

# plt.legend()
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.show()

# #! 좋은 모델과 안좋은 모델 참조) https://kevinthegrey.tistory.com/136
