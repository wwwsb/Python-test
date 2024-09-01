person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

#取得键的值
print(person.get('name'))



#update()方法更新键值对
person1 = {'name': 'Alice', 'age': 25}
update_info = {'city': 'New York', 'age': 26}
person1.update(update_info)
print(person1)


person.update({'apple':23})
print(person)

person.pop("apple")
print(person)