from collections import Counter

# 计算文件单词的频率
with open(r'E:/桌面文件/文本笔记/Linux基本操作.txt', encoding="utf-8") as f:
    p = Counter(f.read().split())
    print(p)
