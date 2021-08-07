# 操作字典运算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 计算一般通过zip实现反转key-value
pp = zip(prices.values(), prices.keys())
min_price = min(pp)
print(min_price)
# zip只能访问一次   print(min(pp))---ValueError: min() arg is an empty sequence
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 直接使用min/max
min_val = prices[min(prices,key = lambda k:prices[k])]
print(min_val)