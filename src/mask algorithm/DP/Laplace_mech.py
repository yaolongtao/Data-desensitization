import numpy as np
import pandas as pd


def noisyCount(sensitivety, epsilon):
    beta = sensitivety / epsilon
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        n_value = -beta * np.log(1 - u2)
    else:
        n_value = beta * np.log(u2)
    return n_value


def laplace_mech(data, sensitivety, epsilon):
    for i in range(len(data)):
        data[i] += noisyCount(sensitivety, epsilon)
    return data


filename = pd.read_csv('./data/15年体测.csv')
high = filename["身高"]
high1 = []
for i in high:
    high1.append(i)
# print(high)
# print(high1)
# high_df = high.to_frame()
# print(high)
# x = [1, 2, 3, 4, 5, 6]
# a = len(high_df)
# print(a)
sensitivety = 1
epsilon = np.log(10)
data = laplace_mech(high1, sensitivety, epsilon)
filename["身高"] = data
# print(filename)
filename.to_csv("差分隐私后15体测.csv", index=False)
# for j in data:
#     print("%.2f" % j)
