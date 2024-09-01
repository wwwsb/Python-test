# and or not

# and的使用
temp = float(input("输入温度："))
# if temp > 0 and temp < 30:
#     print("温度是合适的")
# else:
#     print("不适宜")

#or的使用
if temp <= 0 or temp >= 30:
    print("温度是合适的")
else:
    print("不适宜")

#not的使用
print(not True)   # 输出：False
print(not False)  # 输出：True

x = 10
if not x > 5:#flase
    print("x is not greater than 5")
else:
    print("x is greater than 5")

