#键 值

# 空字典
empty_dict = {}

# 含有元素的字典
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
print(person)
# 输出：{'name': 'Alice', 'age': 25, 'city': 'New York'}

# 使用键值对参数
person = dict(name='Bob', age=30, city='Los Angeles')
print(person)
# 输出：{'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}

# 使用包含元组的列表
person = dict([('name', 'Charlie'), ('age', 28), ('city', 'Chicago')])
print(person)
# 输出：{'name': 'Charlie', 'age': 28, 'city': 'Chicago'}


person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(person['name'])  # 输出：Alice
print(person['age'])   # 输出：25

print(person.get('name'))     # 输出：Alice
print(person.get('gender'))   # 输出：None
print(person.get('gender', 'Not specified'))  # 输出：Not specified

#添加键值对
person = {'name': 'Alice', 'age': 25}

# 添加新键值对
person['city'] = 'New York'
print(person)
# 输出：{'name': 'Alice', 'age': 25, 'city': 'New York'}

#修改已有键值对
person['age'] = 26
print(person)
# 输出：{'name': 'Alice', 'age': 26, 'city': 'New York'}

#删除字典元素
del person['city']
print(person)
# 输出：{'name': 'Alice', 'age': 26}

#pop() 方法删除指定键并返回对应的值。
age = person.pop('age')
print(age)     # 输出：26
print(person)  # 输出：{'name': 'Alice'}


person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
keys = person.keys()
print(keys)  # 输出：dict_keys(['name', 'age', 'city'])


values = person.values()
print(values)  # 输出：dict_values(['Alice', 25, 'New York'])

items = person.items()
print(items)  
# 输出：dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

#将一个字典的键值对更新到另一个字典中。
person = {'name': 'Alice', 'age': 25}
update_info = {'city': 'New York', 'age': 26}
person.update(update_info)
print(person)
# 输出：{'name': 'Alice', 'age': 26, 'city': 'New York'}


person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in person:
    print(key)
# 输出：
# name
# age
# city


for value in person.values():
    print(value)
# 输出：
# Alice
# 25
# New York

for key, value in person.items():
    print(f"{key}: {value}")
# 输出：
# name: Alice
# age: 25
# city: New York





