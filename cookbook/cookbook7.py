# 删除序列相同元素并保持顺序，直接使用集合set不能保证顺序

def dedupe(items):  # 仅在元素是hashable时候才可用
    seen = set()
    for i in items:
        if i not in seen:
            yield i  # 生成器 --迭代的return
            seen.add(i)


def dedupe1(items, key=None):  # 元素不可哈希，例如dict
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


bb = list(dedupe([1, 1, 1, 1, 1, 2, 3, 5, 8, 6, 8, 4, 5, 6]))
print(bb)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

cc = list(dedupe1(a, key=lambda d: (d['x'], d['y'])))
dd = list(dedupe1(a, key=lambda d: d['x']))
print(cc)
print(dd)
