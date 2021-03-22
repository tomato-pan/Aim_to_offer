"""
一根绳子，长度为n米。将其切成几段，每一段的长度都是整数。请给出一种切法，使得切成的各段绳子之间的乘积是最大的。注意，最少要切一下的。
"""


class Solution:
    def find_max(self, target):
        if target <= 1: return 0
        if target == 2: return 1
        if target == 3: return 2
        if target == 4: return 4
        x = target // 3
        res = target - x * 3
        if res == 0: res = 1
        if target - x * 3 == 1:
            x -= 1
            res = 4
        for i in range(1, x + 1):
            res = res * 3
        return res

    # dp
    def find_max1(self, n):
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.find_max(6))
