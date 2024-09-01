goods = []
prices = []
while True:
    good = input("请输入商品:")

    if good.lower() == 'q':
        break
    price = float(input("请输入价格:"))

    goods.append(good)
    prices.append(price)
print('商品：',goods)
print("价格：",prices)

for index,good in enumerate(goods):
    print(f'第{index+1}个商品为{good},价格为{prices[index]}')

total_price = sum(prices)
print(f"总价格：{total_price}")