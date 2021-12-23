import math
import time


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        if n <= 2: return n
        c = 0
        a = 1
        b = 2
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c

    def climbStairs1(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        finb = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(finb / sqrt5)

    def count_sum(self, items: list):
        overall = partial = items[0]
        for i in range(1, len(items)):
            partial = max(items[i], partial + items[i])
            print(partial)
            overall = max(partial, overall)
        return overall

    def fib(self, n: int) -> int:
        if (n <= 2): return 1
        return self.fib(n - 1) + self.fib(n - 2)

    dic_fib = {}

    def fib1(self, n: int) -> int:
        if self.dic_fib.get(n): return self.dic_fib[n]
        if (n <= 2): return 1
        self.dic_fib[n] = self.fib1(n - 1) + self.fib1(n - 2)
        return self.fib1(n - 1) + self.fib1(n - 2)


if __name__ == '__main__':
    list1 = [0, -2, 1, -1, 5, -3, 2]
    s = Solution()
    # print(s.climbStairs(2))
    # print(s.climbStairs1(2))
    # print(s.count_sum(list1))
    t1 = time.time()
    print(s.climbStairs1(100))
    t2 = time.time()
    print("cost:%d" % (t2 - t1))
    print(s.climbStairs2(100))
    print("cost:%d" % (time.time() - t2))
