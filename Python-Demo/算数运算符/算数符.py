#python中的数学
apple_num = int(input('苹果数量：'))
apple_num += 1
print(apple_num)

apple_num *= 2
print(apple_num)

apple_num = apple_num ** 3 #三次方
print(apple_num)

#除余
num = 10
print(num%3)#除余10/3=3>>>1

#次方内置函数 pow()
print(pow(2,3))#2的3次方
a = 2
a = pow(a,4)
print(a)

#最大值max()和最小值min()

print(max(12,45,3))
print(min(0,1))

#四舍五入函数round()
print(round(3.5))  #输出4
print(round(3.334454,3))#输出3.334   其中3为保留三位小数

#绝对值函数 abs()
print(abs(-32))


#Π   计算周长
import math

print(math.pi)
radis = float(input("半径："))
zhouchang  = 2*math.pi*radis
print(f"圆的周长：{zhouchang:.2f}")#保留两位数字
print(f"圆的周长：",round(zhouchang,3))#保留三位
print(f"圆的周长：",round(zhouchang))#保留整数

