import numpy as np
import pandas as pd


# 简单的问候语
def SimpleGreeting():
    for i in range(10):
        print(str(i) + ':hello world!')
    print("greeting end.")


# 普通python输出文件方法
def FileOutputMethod1():
    list = [['西瓜', '兰州', 'first', 20], ['香蕉', '西安', 'second', 30], ['苹果', '银川', 'third', 40],
            ['桔子', '四川', 'fourth', 40]]
    output = open("C:/Users/姚龙涛/Desktop/data.xls", "w", encoding="gbk")
    output.write('fruit\t place\t digital\t number\n')
    for i in range(len(list)):
        for j in range(len(list[i])):
            output.write(str(list[i][j]))
            output.write('\t')
        output.write('\n')
    output.close()


# 利用numpy实现数组输出为文件，不能实现字符串输出为文件
def FileOutputMethod2():
    list1 = [[1, 2, 3], [4, 5, 6]]
    np.savetxt('C:/Users/姚龙涛/Desktop/data1.txt', list1, fmt='%.8f')


# 调用pandas库写输出文件，效果最好，推荐方法
def FileOutputMethod3():
    list2 = [['yaolongtao', 2, 3], [4, 5, 6]]
    df = pd.DataFrame(list2)
    df.to_csv("C:/Users/姚龙涛/Desktop/data2.csv", sep=',', header=False, index=False)


SimpleGreeting()
# FileOutputMethod1()
# FileOutputMethod2()
# FileOutputMethod3()
