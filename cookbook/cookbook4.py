# 1.6 字典中的键映射多个值

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

c= defaultdict(set)
c['a'].add(1)
c['a'].add(2)
c['b'].add(4)

print(d,c)

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
