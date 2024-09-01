import time

my_time = int(input("请输入秒数："))

for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)
print("时间到",time.time())


# time.sleep(2)