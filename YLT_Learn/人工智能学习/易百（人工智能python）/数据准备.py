import numpy as np
from sklearn import preprocessing

# 二值化数据
input_data = np.array([[2.1, -1.9, 5.5],
                       [-1.5, 2.4, 3.5],
                       [0.5, -7.9, 5.6],
                       [5.9, 2.3, -5.8]])
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)
# 平均去除
print("Mean=", input_data.mean(axis=0))  # 平均值
print("Std deviation=", input_data.std(axis=0))  # 标准差
data_scaled = preprocessing.scale(input_data)
print("Mean=", data_scaled.mean(axis=0))
print("Std deviation=", data_scaled.std(axis=0))
# 最大最小缩放
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)
# 正常化：L1标准化-最小绝对偏差，L2标准化-最小二乘
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
print("\nL1 normalized data:\n", data_normalized_l1)
data_normalized_l2=preprocessing.normalize(input_data,norm='l2')
print("\nL2 normalized data:\n",data_normalized_l2)