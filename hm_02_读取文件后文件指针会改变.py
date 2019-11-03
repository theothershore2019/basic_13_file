# 1.打开文件
file = open("README")

# 2.读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

# 第一次读取之后，文件指针移动到了文件末尾，再次调用 read 方法不会读取到任何的内容
text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()
