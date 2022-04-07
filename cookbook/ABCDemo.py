from abc import ABC


class MyABC(ABC):
    pass


MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)


def cal_cans(s, query):
    can_list = []
    for q in query:
        print(s[q[0]:q[1] + 1])
        can_list.append(cal_can(s[q[0]:q[1] + 1]))
    return can_list


def cal_can(s):
    queue = []



if __name__ == '__main__':
    s = "**|**|***|"
    queries = [[2, 9]]
    print(cal_cans(s, queries))
