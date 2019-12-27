import numpy as np

lst = [[1, 3, 5], [2, 4, 6]]
print(type(lst))
np_lst = np.array(lst)
print(type(np_lst))
np_lst = np.array(lst, dtype=np.float)
# bool,int,int8,int16,int32,int64,int128,uint8,uint16,uint32,uint64,uint128;
# float,float16/32/64,complex64/128
print(np_lst.shape)
print(np_lst.ndim)
print(np_lst.dtype)
print(np_lst.itemsize)
print(np_lst.size)
# 2 Some Arrays
print(np.zeros([2, 4]))
print(np.ones([3, 5]))
print(np.random.rand(2, 4))
print(np.random.rand())
print("RandInt:")
print(np.random.randint(1, 10, 3))
print("Randn:")
print(np.random.rand(2, 4))
print("Choice:")
print(np.random.choice([10, 20, 30, 1, 3, 5]))
print("Distribute:")
print(np.random.beta(1, 10, 100))
# 3 Array Opes
lst = np.arange(1, 11).reshape([5, -1])
print(np.exp(lst))
print(np.exp2(lst))
print(np.sqrt(lst))
print(np.sin(lst))
print("Log")
print(np.log(lst))
lst = np.array([[[1, 2, 3, 4],
                 [4, 5, 6, 7]],
                [[7, 8, 9, 10],
                 [11, 12, 13, 14]],
                [[15, 16, 17, 18],
                 [19, 20, 21, 22]]
                ])
print("Sum")
print(lst.sum(axis=2))
print("Max")
print(lst.max(axis=2))
print("Min")
print(lst.min(axis=2))
lst1 = np.array([10, 20, 30, 40])
lst2 = np.array([4, 3, 2, 1])
print("Add")
print(lst1 + lst2)
print("Sub")
print(lst1 - lst2)
print("Mul")
print(lst1 * lst2)
print("Div")
print(lst1 / lst2)
print("Square")
print(lst1 ** 2)
print("Dot")
print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))
print("Cancatenate")
print(np.concatenate((lst1, lst2), axis=0))
print(np.vstack((lst1, lst2)))
print(np.hstack((lst1, lst2)))
print(np.split(lst1, 4))
print(np.copy(lst1))
# 4 liner
from numpy.linalg import *

print(np.eye(3))
lst = np.array([[1, 2],
                [3, 4]])
print("Inv")
print(inv(lst))
print("T:")
print(lst.transpose())
print("Det:")
print(det(lst))
print(eig(lst))
y=np.array([[5],[7]])
print(solve(lst,y))
#5 Others
print("FFT")
print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))
print("Coef:")
print(np.corrcoef([1,0,1],[0,2,1]))
print("Poly:")
print(np.poly1d([2,1,3]))