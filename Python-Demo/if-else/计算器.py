
oppera = input("请输入要使用的运算符+-*/:")
a,b =map(float,input('输入数字：').split())
if oppera == "+":
    print(f"{a}+{b}=",a+b)
elif oppera =="-":
    print(f"{a}-{b}=",a-b)
elif oppera =="*":
    print(f"{a}*{b}=",a*b)
elif oppera =="/":
    print(f"{a}/{b}=",a/b)
else:
    print("输入错误")
