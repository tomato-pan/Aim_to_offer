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
    if f[target] == target + 1:
        return -1
    else:
        return f[target]


def dp_tri(numRows: int) -> List:
    result = []
    for i in range(numRows):
        now = [1] * (i + 1)
        if i >= 2:
            for n in range(1, i):
                now[n] = pre[n - 1] + pre[n]
        result += [now]
        pre = now
        print(result)
    return result


def generate(numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows):
        res.append([0] * (i + 1))
    for i in range(numRows):
        for j in range(len(res[i])):
            if j == 0 or i == j:
                res[i][j] = 1
            else:
                res[i][j] = res[i - 1][j] + res[i - 1][j - 1]
    return res


def duplicate_zeros(nums: List[int]):
    pass


def findRepeatNumber(nums: List[int]) -> int:
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return nums[i]
        dic[nums[i]] = i


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) //2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle-1
        else:
            return middle
    return -1


if __name__ == '__main__':
    # print(dp1([1, 2, 5], 21))
    # print(dp1([3], 4))
    # dp_tri(5)
    print(findRepeatNumber([0, 10, 2, 0, 2, 1, 3, 1, 5, 3]))
    print(search(nums=[5],target=5))
