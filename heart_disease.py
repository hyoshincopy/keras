import functools
import pandas as pd
import tensorflow as tf
import numpy as np

#! csv 파일을 불러오는 법
df = pd.read_csv("./heart.csv")
print(1)

# ! 데이터 자료형 확인하는 방법 print(df.dtypes)
df.thal = pd.Categorical(df.thal)  # * 'thal' 열은 혼자 object 이므로 이산숫자로 변환해줘야한다
df.thal = df.thal.cat.codes  # * 이산숫자로 변환하기위해서는 먼저 카테고리컬 형태로 바꾸어주고 cat.codes를 사용한다

# ? 이 데이터 프레임에는 feature 컬럼 여러개와
# ? target 컬럼 한개로 구성되어있다.
# ? feature 는 input, target은 label 이라고 생각하면 된다


target = df.pop('target')  # *  레이블만 따로 떼어서 저장하자

dataset = tf.data.Dataset.from_tensor_slices(

    (df.values, target.values)

)

# * dataset.take(5) 를 사용하여 dataset에 들어있는 다섯개의 데이터를 출력
for feat, targ in dataset.take(5):
    print('F:{}, T: {}'.format(feat, targ))

train_dataset = dataset.shuffle(len(df)).batch(1)  # * 데이터셋을 섞고 묶는다


def get_compiled_model():
    model = tf.keras.Sequential([

        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')

    ])

    model.compile(optimizer='adam', loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model


model = get_compiled_model()
model.fit(train_dataset, epochs=15)
