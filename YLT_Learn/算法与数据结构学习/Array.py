import time


def removeDuplicates(nums):
    if len(nums) == 0:
        print(0)
    slow = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[slow]:
            slow += 1
            nums[slow] = nums[i]
    print(slow + 1)


def maxProfit(prices):
    sum = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            sum += prices[i + 1] - prices[i]
    print(sum)


def rotate1(nums, k):
    if len(nums) == 0 or k == 0:
        print(nums)
    else:
        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        n = len(nums) - 1
        k = k % len(nums)
        reverse(0, n - k, nums)
        print(nums)
        reverse(n - k + 1, n, nums)
        print(nums)
        reverse(0, n, nums)
        print(nums)


def rotate2(nums, k):
    k = k % len(nums)
    # right = nums[-k:]
    # nums[k:] = nums[0:-k]
    # nums[0:k] = right
    nums[:] = nums[-k:] + nums[:-k]
    print(nums)


def rotateMatrix(matrix):
    if len(matrix) == 0:
        print("该矩阵为空")
    h = len(matrix)
    w = len(matrix[0])
    for i in range(h):
        # 需要注意的是j从i+1开始遍历！！
        for j in range(i + 1, w):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(h):
        for j in range(w // 2):
            matrix[i][w - 1 - j], matrix[i][j] = matrix[i][j], matrix[i][w - 1 - j]

    print(matrix)


def testTime():
    start = time.clock()
    # 测试代码所放地方
    end = time.clock()
    print(str((end - start) * 1000) + "ms")


# 从排序数组中删除重复项
# removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# 买卖股票的最佳时机II
# maxProfit([7, 1, 5, 3, 6, 4])
# 旋转数组
# rotate1([1, 2, 3, 4, 5, 6, 7], 3)
# rotate2([-1, -100, 3, 99], 2)
# 旋转图像
rotateMatrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
rotateMatrix([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
])
