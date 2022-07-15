from typing import List


def numWays(n: int) -> int:
    f = [0] * (n + 1)
    if n == 0: return 0
    if n == 1: return 1
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 1000000007
    return f[n]


def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums


def pivotIndex(nums: List[int]) -> int:
    #求和
    half = int(sum(nums)/2)
    for i in range(len(nums)):
        if (sum(nums[:i])+nums[i]) == half:
            return i
    return -1


print(numWays(7))
print(runningSum([1, 2, 3, 4]))
print(pivotIndex([1, 7, 3, 6, 5, 6]))
