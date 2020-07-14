# import functools
import pandas as pd
import tensorflow as tf

df = pd.read_csv("./heart.csv")


df.thal = pd.Categorical(df.thal)  # * 'thal' 열은 혼자 object 이므로 이산숫자로 변환해줘야한다
df.thal = df.thal.cat.codes  # * 이산숫자로 변환하기위해서는 먼저 카테고리컬 형태로 바꾸어주고 cat.codes를 사용한다

# ? 이 데이터 프레임에는 feature 컬럼 여러개와
# ? target 컬럼 한개로 구성되어있다.
# ? feature 는 input, target은 label 이라고 생각하면 된다

# import numpy as np
# import keras
# import tensorflow as tf
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(10, input_shape=[1, 35]),
#     tf.keras.layers.Dense(10, activation='relu'),
#     tf.keras.layers.Dense(20, activation='softmax')
# ])


# train_file_path = tf.keras.utils.get_file()
# test_file_path = tf.keras.utils.get_file("b.csv", TEST_DATA_URL)

# tf.keras.utils
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])


# model.fit(x_train, y_label, epochs=5)
