# 命名切片
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost1 = int(record[SHARES]) * float(record[PRICE])
print(cost1)