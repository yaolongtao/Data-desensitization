import matplotlib.pyplot as plt
import numpy as np
import math

# plt.rcParams['axes.unicode_minus'] = False  # 步骤二(解决坐标轴负数的负号显示问题)
#
# x = np.arange(0, math.pi * 2, 0.05)
# y = np.sin(x)
# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y)
# ax.set_title("正弦波")
# ax.set_xlabel("角度")
# ax.set_ylabel("正弦")

plt.show()
loc, scale = 0., 1.
s = np.random.laplace(loc, scale, 1)
ss = s[0]

print(ss)