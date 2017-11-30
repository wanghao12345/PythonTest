# 文件基本操作
#
# 1.打开文件
#  file_obj = open("文件路径","模式")
#  常用的打开文件模式有：
#     r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#     w：打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#     a：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#     w+：打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#
# 2.读取文件的内容
#   obj.read()：一次性加载所有内容到内存
#   obj.readLines()：一次性加载所有内容到内存，并根据行分割成字符串
#   for line in obj:
#       print line
#       -------------每次仅读取一行数据
#
# 3.写文件的内容
#   obj.write('内容')：给文件写入内容
#
# 4.关闭文件句柄
#   obj.close()：关闭文件

# 写
# obj = open("test.log","w")
# obj.write("This is the first line\n")
# obj.write("This is the second line\n")
# obj.close()

# 读
# obj = open("test.log","r")
# for line in obj:
#     print(line)
# obj.close()

# 追加
# obj = open("test.log","a")
# obj.write("This is the three line\n")
# obj.close()

# 写读
# obj = open("test.log","w+")
# obj.write("new line\n")
# print("data:",obj.read())
# obj.close()