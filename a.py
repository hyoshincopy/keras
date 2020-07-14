# import functools
import pandas as pd
import tensorflow as tf
import numpy as np
df = pd.read_csv("./heart.csv")


df.thal = pd.Categorical(df.thal)  # * 'thal' 열은 혼자 object 이므로 이산숫자로 변환해줘야한다
df.thal = df.thal.cat.codes  # * 이산숫자로 변환하기위해서는 먼저 카테고리컬 형태로 바꾸어주고 cat.codes를 사용한다

# ? 이 데이터 프레임에는 feature 컬럼 여러개와
# ? target 컬럼 한개로 구성되어있다.
# ? feature 는 input, target은 label 이라고 생각하면 된다


target = df.pop('target')  # *  레이블만 따로 떼어서 저장하자

dataset = tf.data.Dataset.from_tensor_slices(

    (df.values, target.values)

)

for feat, targ in dataset.take(5):
    print('F:{}, T: {}'.format(feat, targ))
