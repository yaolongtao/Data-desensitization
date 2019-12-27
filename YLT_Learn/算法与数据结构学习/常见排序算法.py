# def BubbleSort(ls):
#     n = len(ls)
#     if n <= 1:
#         return ls
#     for i in range(0, n):
#         for j in range(0, n - i - 1):
#             if ls[j] > ls[j + 1]:
#                 (ls[j], ls[j + 1]) = (ls[j + 1], ls[j])
#     return ls
#
#
# x = input("请输入待排序数列：\n")
# y = x.split()
# arr = []
# for i in y:
#     arr.append(int(i))
# arr = BubbleSort(arr)
# # print(arr)
# print("数列按序排列如下：")
# for i in arr:
#     print(i, end=' ')
# 1.冒泡排序
def Bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# 2.选择排序
def Selection_sort(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n - 1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


#  3.插入排序
def Insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


# 4.快速排序
def Quick_sort(alist, start, end):
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
        # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    Quick_sort(alist, start, low - 1)
    # 对基准元素右边的子序列进行快速排序
    Quick_sort(alist, low + 1, end)


#  5.希尔排序
def Shell_sort(alist):
    n = len(alist)
    # 用//代替/,不然默认得到float类型
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        # 得到新的步长
        gap = gap // 2


# 6.归并排序
def Merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    num = len(alist) // 2
    left = Merge_sort(alist[:num])
    right = Merge_sort(alist[num:])
    # 合并
    return merge(left, right)


def merge(left, right):
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(Merge_sort(li))
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
Quick_sort(alist, 0, len(alist) - 1)
print(alist)
