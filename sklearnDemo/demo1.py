from typing import List

from sklearn.ensemble import RandomForestClassifier


def demo():
    clf = RandomForestClassifier(random_state=0)
    x = [[1, 2, 3],
         [3, 4, 6]]
    y = [0, 1]
    print(clf.fit(x, y))
    print(clf.predict(x))


def dp1(coins: List, target: int) -> int:
    f = [target + 1] * (target + 1)
    f[0] = 0
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin < 0: continue
            f[i] = min(f[i - coin] + 1, f[i])
    if f[target] == target+1 :return -1
    else: return f[target]


if __name__ == '__main__':
    print(dp1([1, 2, 5], 21))
    print(dp1([3], 4))
