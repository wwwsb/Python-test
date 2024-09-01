#字串的方法
name = "le py"

#判断长度len()函数
length = len(name)
print(f"字符长度:{length}")

"""
find() 是 Python 字符串方法之一，用于在字符串中查找子字符串的位置。
它返回子字符串在字符串中第一次出现的索引（位置），
如果未找到子字符串，则返回 -1。
"""
space_o = name.find(" ")
print(f"字符第一个空格:{space_o}")

text = "Hello,world!"
index = text.find("world")
print(index)  # 输出：6

#指定起始位置;在这个例子中，我们从索引 10 开始查找 "Hello"，find() 返回第二个 "Hello" 的起始位置 12。
text = "Hello,world!Hello,everyone!"
index = text.find("Hello", 10)
print(index)  # 输出：12


#指定起始和结束位置
text = "Hello, world! Hello, everyone!"
index = text.find("Hello", 10, 20)
print(index)  # 输出：14

#capitalize() 是一个字符串方法，用于将字符串的第一个字符转换为大写字母，
# 同时将字符串中其余的字符转换为小写字母。
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # 输出：Hello world

text = "123hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # 输出：123hello world

#title()方法将字符串中每个单词的首字母都转换为大写，而不仅仅是第一个字母
text = "hello world"
title_text = text.title()
print(title_text)  # 输出：Hello World

#cout函数：用于计算某个子字符串或元素在序列中出现的次数。

text = "hello world, hello everyone"
count_hello = text.count("hello")
print(count_hello)  # 输出：2

#使用start和end
text = "hello world, hello everyone"
count_hello = text.count("hello", 5, 20)
print(count_hello)  # 输出：1

numbers = [1, 2, 3, 4]
count_three = numbers.count(3)
print(count_three)  # 输出：3

#replace方法  str.replace(old, new[, count])

number = "nihaohh"
number = number.replace('h','H')
print(number)
#限制替换次数
number = "nihaohh"
number = number.replace('h','H',1)
print(number)




