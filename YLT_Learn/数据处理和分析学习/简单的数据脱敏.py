# 读取文件
sourcefilepath = "data/脱敏前数据.txt"
with open(sourcefilepath, 'r', encoding='utf-8') as f:
    contents = f.readlines()
# 指定替代列及替代字符
column_num = 3
replace_key = '-----'
# 存储文件
output = open("data/脱敏后数据.txt", "w", encoding="utf-8")
flag = 0
# 字符替代处理
for line in contents:
    flag += 1
    temp = line.split("|")
    temp[column_num - 1] = replace_key
    target_line = ""
    # len(temp) - 1为不在最后换行符后面加'|'
    for i in range(len(temp) - 1):
        target = temp[i] + "|"
        # 列表中几个字符串拼接为一长串
        target_line += target
    result = str(flag) + ": " + target_line
    output.write(result)
    output.write('\n')
    print(result)
output.close()
