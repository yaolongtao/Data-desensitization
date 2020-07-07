# 读取文件
sourcefilepath = "data/Donor_100.txt"
with open(sourcefilepath, 'r', encoding='utf-8') as f:
    contents = f.readlines()


def mask_1(a):
    # 指定替代列及替代字符
    column_num = a
    replace_key = '******'
    # 存储文件
    output = open("data/献血码掩码.txt", "w", encoding="utf-8")
    flag = 0
    # 字符替代处理
    for line in contents:
        flag += 1
        temp = line.split(",")
        temp[column_num - a] = temp[column_num - 1][0:3] + replace_key + temp[column_num - 1][-4:]
        target_line = ""
        # len(temp) - 1为不在最后换行符后面加','
        for i in range(len(temp) - 1):
            target = temp[i] + "，"
            # 列表中几个字符串拼接为一长串
            target_line += target
        result = target_line
        output.write(result)
        output.write('\n')
        print(result)


def mask_2(b):
    # 指定替代列及替代字符
    column_num = b
    replace_key = '**'
    # 存储文件
    output = open("data/姓名掩码.txt", "w", encoding="utf-8")
    flag = 0
    # 字符替代处理
    for line in contents:
        flag += 1
        temp = line.split(",")
        temp[column_num - 1] = temp[column_num - 1][0:1] + replace_key
        target_line = ""
        # len(temp) - 1为不在最后换行符后面加','
        for i in range(len(temp) - 1):
            target = temp[i] + "，"
            # 列表中几个字符串拼接为一长串
            target_line += target
        result = target_line
        output.write(result)
        output.write('\n')
        print(result)


def mask_3(c):
    # 指定替代列及替代字符
    column_num = c
    replace_key = '********'
    # 存储文件
    output = open("data/身份证号掩码.txt", "w", encoding="utf-8")
    flag = 0
    # 字符替代处理
    for line in contents:
        flag += 1
        temp = line.split(",")
        temp[column_num - 1] = temp[column_num - 1][0:8] + replace_key + temp[column_num - 1][-2:]
        target_line = ""
        # len(temp) - 1为不在最后换行符后面加','
        for i in range(len(temp) - 1):
            target = temp[i] + "，"
            # 列表中几个字符串拼接为一长串
            target_line += target
        result = target_line
        output.write(result)
        output.write('\n')
        print(result)


def mask_4(d):
    # 指定替代列及替代字符
    column_num = d
    output = open("data/地址掩码.txt", "w", encoding="utf-8")
    flag = 0
    # 字符替代处理
    for line in contents:
        flag += 1
        temp = line.split(",")
        half = len(temp[column_num - 1])
        temp[column_num - 1] = temp[column_num - 1][0:half] + '*' * half
        target_line = ""
        # len(temp) - 1为不在最后换行符后面加','
        for i in range(len(temp) - 1):
            target = temp[i] + "，"
            # 列表中几个字符串拼接为一长串
            target_line += target
        result = target_line
        output.write(result)
        output.write('\n')
        print(result)

# mask_1(1)
# mask_2(2)
# mask_3(3)
# mask_4(4)
