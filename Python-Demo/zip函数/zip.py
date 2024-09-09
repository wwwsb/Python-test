"""
zip函数用于将多个可迭代对象(列表、元组)打包成一个元组的迭代器
每个元组中的元素来自于传入的可迭代对象的对应位置。简单来说，zip() 可以将多个列表按元素一一配对，形成多个元组。


"""
list1 = [1,2,3]
list2 = ['a','b','c'] 
# 使用 zip() 将两个列表打包
zipped = zip(list1,list2)
# 转换为列表以查看结果
print(list(zipped))

#zip() 经常用于遍历多个可迭代对象时，同时获取对应位置的元素

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} got {score} points.")
