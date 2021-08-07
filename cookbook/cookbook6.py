# 查找两字典的相同点

def find_com(a: dict, b: dict):
    print(a.keys() & b.keys())  # 仅key相同的 keys()可以直接和set一样的运算
    print(a.items() & b.items())# key-value均相同
    # values()不推荐直接运算


if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    find_com(a, b)
