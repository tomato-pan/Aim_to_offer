data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, _, date = data # 迭代赋值单变量
print(name)
*a,date1 = data # 多变量
print(date1)