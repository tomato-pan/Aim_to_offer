class Solution:
    def hammingWeight(self, n: int) -> int:
        sum1 = 0
        while n != 0:
            sum1 += 1
            n = n & n - 1
        return sum1

    def hammingWeight1(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1  # n与1与运算
            n = n >> 1  # 右移一位
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.hammingWeight1(100))
