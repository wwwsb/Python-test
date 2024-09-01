num = int(input("请输入1-10之间数字："))
while num not in [1,2,3,4,5,6,7,8,9,10]:
    print("输入无效,请输入1-10之间数字")
    num = int(input("请输入1-10之间数字："))
print(f"输入数字为{num}")