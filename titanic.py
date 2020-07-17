import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#! xls 파일을 불러오는 법
raw_data = pd.read_excel('titanic.xls')
#! 불러온 파일 정보 확인
# raw_data.info()

# print(raw_data.describe())
print(type(raw_data))
