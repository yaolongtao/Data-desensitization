import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 解决图片不能显示负数问题
matplotlib.rcParams['axes.unicode_minus'] = False


# 定义拉普拉斯函数
def laplace_function(x, u, b):
    result = (1 / (2 * b)) * np.e ** (-1 * (np.abs(x - u) / b))
    return result


# 定义高斯函数
def gaussian_function(x, u, v):
    result = (1 / math.sqrt(2 * 3.1415926 * v)) * np.e ** (-1 * (x - u) * (x - u) / v ** 2)
    return result


# 定义指数函数
def exponential_function(x, u):
    result = u * np.e ** (-1 * u * x)
    return result


# 显示拉普拉斯分布图像
x = np.linspace(-5, 5, 10000)
y1 = [laplace_function(x_, 0, 0.5) for x_ in x]
y2 = [laplace_function(x_, 0, 1) for x_ in x]
y3 = [laplace_function(x_, 0, 2) for x_ in x]
y4 = [laplace_function(x_, -2, 1) for x_ in x]
plt.plot(x, y1, color='r', label='u:0,b:0.5')
plt.plot(x, y2, color='g', label='u:0,b:1')
plt.plot(x, y3, color='b', label='u:0,b:2')
plt.plot(x, y4, color='k', label='u:-2,b:1')
plt.title("拉普拉斯分布")
plt.legend()
plt.show()

# 显示高斯分布图像
z1 = [gaussian_function(x_, 0, 0.5) for x_ in x]
z2 = [gaussian_function(x_, 0, 1) for x_ in x]
z3 = [gaussian_function(x_, 0, 2) for x_ in x]
z4 = [gaussian_function(x_, -2, 1) for x_ in x]
plt.plot(x, z1, color='r', label='u:0,v:0.5')
plt.plot(x, z2, color='g', label='u:0,v:1')
plt.plot(x, z3, color='b', label='u:0,v:2')
plt.plot(x, z4, color='k', label='u:-2,v:1')
plt.title("高斯分布")
plt.legend()
plt.show()

# 显示指数分布图像
x = np.linspace(0, 5, 5000)
w1 = [exponential_function(x_, 0.5) for x_ in x]
w2 = [exponential_function(x_, 1) for x_ in x]
w3 = [exponential_function(x_, 2) for x_ in x]
plt.plot(x, w1, color='r', label='u:0.5')
plt.plot(x, w2, color='g', label='u:1')
plt.plot(x, w3, color='b', label='u:2')
plt.title("指数分布")
plt.legend()
plt.show()
