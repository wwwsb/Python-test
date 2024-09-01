"""
在Python中，单下划线 _ 通常用作一个临时的、占位符的变量名，表示“我不关心这个值”或者“我不会使用这个值”。
这种用法在解包（unpacking）多个返回值的情况下特别常见。
"""


def some_function():
    return 10, 20, 30

# 你只关心第三个返回值
_, _, value = some_function()
print(value)  # 输出：30

for _ in range(5):
    print("Hello")

data = (1, 2, 3, 4, 5)
_, second, _, fourth, _ = data
print(second, fourth)  # 输出：2 4
