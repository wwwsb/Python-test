#for使用
#in后面跟可迭代的对象：
# 列表[1, 2, 3, 4]，
# 元组：(1, 2, 3, 4)
#字符串，字典：{"a": 1, "b": 2, "c": 3}，
# 集合：{1, 2, 3, 4}
# 生成器和迭代器
for i in range(1,10):
    print(i)

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # 输出：True
print(6 in numbers)  # 输出：False

#在元组中使用in
colors = ('red', 'green', 'blue')
print('green' in colors)  # 输出：True
print('yellow' in colors)  # 输出：False


#倒叙输出
for i in reversed(range(1,10)):
    if i == 3:
        continue
    print(i,end='')
print()
#break的使用
for i in reversed(range(1,10)):
    if i == 3:
        break
    print(i,end='')
print()

#item()的作用
dict = {'a':1,'b':2,'c':3}
for i in dict:
    print(i)


dict = {'a':1,'b':2,'c':3}
for i,j in dict.items():
    print(i,j)

# 输出：
# a 1
# b 2
# c 3


