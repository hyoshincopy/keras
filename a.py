import pandas as pd
import tensorflow as tf

df = pd.read_csv("./heart.csv")

df.thal = pd.Categorical(df.thal)
df.thal = df.thal.cat.codes
print(df.head())
# import functools
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
