"""
enumerate() 是 Python 中的一个内置函数，
用于在遍历可迭代对象（如列表、元组、字符串等）时，
同时获取元素的索引和值。
它返回一个迭代器，迭代器的每个元素是一个包含索引和值的元组。
"""
#遍历列表时获取索引和值
fruit = ["apple","banana",'cherry']
for index,value in enumerate(fruit):
    print(f"索引{index}对应的水果为{value}")

#可以使用 start 参数指定索引的起始值，而不是默认的 0
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits, start=1):
    print(f"索引 {index} 对应的水果是 {value}")
