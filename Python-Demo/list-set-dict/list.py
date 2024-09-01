#列表

# 创建一个列表
my_list = [1, 2, 3, 4, 2]

# 添加元素
my_list.append(5)

# 删除元素
my_list.remove(2)  # 删除第一个出现的2

# 访问元素
print(my_list[0])  # 输出1

# 列表可以包含重复的元素
print(my_list)  # 输出：[1, 3, 4, 2, 5]




fruit = ['apple','banan','baerry']

print(fruit[1])
for i in fruit:
    print(i)

#将元素添加列表append():添加到列表末尾的元素。
fruit.append('orange')
print(fruit)

#remove()要从列表中移除的元素
if 'apple' in fruit:
    fruit.remove('apple')
print(fruit)

#在调用 remove() 之前检查元素是否在列表中

#index()索引
food = ['apple','pizaa','西瓜']
findindex = food.index("西瓜")
print(findindex)

#cout方法
food1 = ['apple','pizaa','西瓜']
food1.append('pizaa')
food1.append('pizaa')
print(food1)
numfood = food1.count('pizaa')
print(numfood)

#列表反转操作为reverse()

