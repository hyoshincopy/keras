
# 출처 https://pinkwink.kr/1119

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#! xls 파일을 불러오는 법
raw_data = pd.read_excel('titanic.xls')
#! 불러온 파일 정보 확인
# raw_data.info()

# ? 그래프로표현
# print(raw_data.describe())
# f, ax = plt.subplots(1, 2, figsize=(12, 6))

# raw_data['survived'].value_counts().plot.pie(
#     explode=[0, 0.1], autopct='%1.2f%%', ax=ax[0])
# ax[0].set_title('circle-graph')
# ax[0].set_ylabel('')

# sns.countplot('survived', data=raw_data, ax=ax[1])
# ax[1].set_title('stick-graph')
# ? 그래프로 표현

# ? 탑승 한 사람들의 전체 연령
# raw_data['age'].hist(bins=20, figsize=(18, 8), grid=False)
# ? 탑승 한 사람들의 전체 연령

# ? pclass 에 따라 정렬
# print(raw_data.groupby('pclass').mean())
# ? pclass 에 따라 정렬

# ? 서로 연관있어 보이는 데이터가 무엇인지 찾기위해 상관계수를 확인
# plt.figure(figsize=(10, 10))
# sns.heatmap(raw_data.corr(), linewidths=0.01, square=True,
#             annot=True, cmap=plt.cm.viridis, linecolor="white")
# plt.title('Correlation between features')
# ? 서로 연관있어 보이는 데이터가 무엇인지 찾기위해 상관계수를 확인
raw_data['age_cat'] = pd.cut(raw_data['age'], bins=[0, 10, 20, 50, 100],
                             include_lowest=True, labels=['baby', 'teenage', 'adult', 'old'])
plt.figure(figsize=[12, 4])  # * figsize 는 가로x세로 인치단위
plt.subplot(131)
sns.barplot('pclass', 'survived', data=raw_data)
plt.subplot(132)
sns.barplot('age_cat', 'survived', data=raw_data)
a = 20
plt.subplot(133)
sns.barplot('sex', 'survived', data=raw_data)
plt.subplots_adjust(top=1, bottom=0.1, left=0.10,
                    right=1, hspace=0.5, wspace=0.5)
plt.show()
