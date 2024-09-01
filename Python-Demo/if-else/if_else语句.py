#if-else流程
#bool值
for_sale = True

#if——else
if for_sale:
    print("在出售")
else:
    print('售空')

age = int(input("输入年龄："))
#判断是否18岁
if age >= 18:
    print("已满18岁")
else:
    print("未满18岁")

#elif
age = int(input("输入年龄："))
if age >= 100:
    print("年龄太大，不能注册")
elif age < 0:
    print("年龄太小，不能注册")   
elif age >= 18:
    print("已满18岁,能注册")

else:
    print("不符合条件,不能注册")