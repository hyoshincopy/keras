import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# * 배열구조나 랜덤값 생성을 위한 numpy
# * 그래프를 그리기 위한 matplotlib

#! 1. 데이터 오브젝트 생성하기
# ? 데이터 오브젝트는 '데이터를 담고 있는 그릇'이다.
# ? pandas에서 자주 사용하는 오브젝트는 Series와 DataFrame이 있다.
# ? Series는 1 차원 배열, DataFrame은 2 차원 배열을 담고있다.
# https://dandyrilla.github.io/2017-08-12/pandas-10min/ 참고
# ? Series는 값의 리스트를 넘겨서 만들 수 있다.
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# ? DataFrame은 여러 형태의 데이터를 받아서 생성 가능하다.
# ? 특히 numpy array 를 받아서 생성을 많이 한다.
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# ? DataFrame을 만들 때는 pd.DataFrame() 이라는 클래스 생성자를 사용한다.
# ? 행에 해당하는 기준을 index 라는 인수로 전달하고
# ? 열에 해당하는 기준을 columns 라는 인수로 전달한다.
#! 2. 데이터 확인하기
# ? 데이터는 df.dtypes 라는 속성을 통해 확인 가능하다
# print(df.dtypes)
# ? 자료들의 맨 앞이나 뒤의 자료들의 몇 개를 알고 싶을 때는 pd.head()와 pd.tail()
# print(df.head())
# ? 인덱스(행)를 보려면 pd.index
# print(df.index)
# ? 컬럼(열)을 보려면 pd.columns
# print(df.columns)
# ? numpy 데이터를 보려면 pd.values
# print(df.values)
# ? pd.describe()는 DataFrame의 간단한 통계정보를 보여준다
# print(df.describe())
# * mean은 평균, std는 표준편차, 25% 50% 75%는 4분위수


df = pd.DataFrame(
    index=["a", "b", "c"],
    columns=["A", "B", "C", "D"])

print(df)
# print(df.loc[df.B == 11]["C"])
