from timeit import Timer

# li1 = [1, 2]
# li2 = [45, 2]
# li = li1 + li2
# li = [i for i in range(10000)]
# li = list(range(10000))


def t1():
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    li = []
    for i in range(10000):
        li += [i]


def t3():
    li = [i for i in range(10000)]


def t4():
    li = list(range(10000))


time1 = Timer("t1()", "from_main_import t1")
print("append:", time1.timeit(1000))
time2 = Timer("t2()", "from_main_import t2")
print("+=", time2.timeit(1000))
time3 = Timer("t3()", "from_main_impo t3")
print("[i for i in range]:", time3.timeit(1000))
time4 = Timer("t4()", "from_main_import t4")
print("list(range):", time4.timeit(1000))
