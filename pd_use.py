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
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# ?
