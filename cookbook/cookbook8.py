# 命名切片
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost1 = int(record[SHARES]) * float(record[PRICE])
print(cost1)
print(SHARES.start, SHARES.step, SHARES.stop)
s = "hello java!!!"
a = slice(5, 10, 2)
cc = a.indices(len(s))  # 不会出现 indexError错误
for i in range(*cc):
    print(s[i])
