
'''
有序性：元组中的元素是有序排列的，可以通过索引访问特定元素。
不可变：元组一旦创建，不能修改其内容（元素不能被增、删、改）。
允许重复：元组可以包含重复的元素。
支持多种数据类型：元组中的元素可以是不同类型的（如整数、字符串、列表、甚至是另一个元组）。
支持嵌套：元组可以包含其他元组或列表作为其元素。
'''

# 创建元组的几种方式
my_tuple = (1, 2, 3)
print(my_tuple)  # 输出：(1, 2, 3)

# 也可以省略括号
my_tuple = 1, 2, 3
print(my_tuple)  # 输出：(1, 2, 3)

# 创建空元组
empty_tuple = ()
print(empty_tuple)  # 输出：()

# 创建单个元素的元组（注意逗号）
single_element_tuple = (5,)
print(single_element_tuple)  # 输出：(5,)

# 不加逗号时，Python会将其视为一个普通的数值表达式
not_a_tuple = (5)
print(not_a_tuple)  # 输出：5

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # 输出：10
print(my_tuple[3])  # 输出：40

# 也可以使用负索引从末尾开始访问
print(my_tuple[-1])  # 输出：50
print(my_tuple[-2])  # 输出：40

my_tuple = (1, 2, 3)

# 尝试修改元组中的元素
# my_tuple[1] = 10  # 会导致 TypeError: 'tuple' object does not support item assignment

tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple = tuple1 + tuple2
print(new_tuple)  # 输出：(1, 2, 3, 4)

my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # 输出：(1, 2, 3, 1, 2, 3)


list1 = [1,2,3]
list2 = [34,5,6]
newlist = list1+list2
print(newlist)



