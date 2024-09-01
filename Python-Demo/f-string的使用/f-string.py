price = 3.1645
print(f"价格为：{price:.2f}")
#加正负号
print(f"价格为：{price:+.2f}")
print(f"价格为：{price:-.2f}")

#对齐
print(f"价格为：{price:5.2f}")
print(f"价格为：{price:5.3f}")

#向左对齐
print(f"价格为：{price:<5.2f}")
print(f"价格为：{price:<5.3f}")

#中对齐
print(f"价格为：{price:^5.2f}")
print(f"价格为：{price:^5.3f}")