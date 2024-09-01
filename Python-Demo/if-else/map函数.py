#map函数的使用

# 将字符串列表转换为整数
str_numbers = ["1", "2", "3"]
int_numbers = map(int, str_numbers)
print(list(int_numbers))  # 输出：[1, 2, 3]

str_numbers = ["10", "20", "30"]
a,b,c = map(int, str_numbers)
print(a,b,c)  # 输出：[1, 2, 3]


# 将列表中的每个元素平方
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # 输出：[1, 4, 9, 16]

#将两个列表中的元素相加
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = map(lambda x, y: x + y, list1, list2)
print(list(summed))  # 输出：[5, 7, 9]
