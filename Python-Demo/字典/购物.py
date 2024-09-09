menu = {
    "pizza":300,
    "apple":20,
    "orange":10
}

print("菜单：")
print("----------")
for key,value in menu.items():
    print(f"{key}:{value}")

while True:
    food = input("请输入，按q退出：")
    if food =="q":
        break
    elif menu.get(food) is None:
        print("无商品")
    else:
        