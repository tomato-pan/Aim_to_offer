from typing import List


class Solution:
    # 第一种 暴力递归
    def coinChange(self, coins: List[int], amount: int) -> int:
        def find_coin(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float("INF")
            for i in coins:
                sub = find_coin(n - i)
                if sub == -1: continue
                res = min(res, 1 + sub)
            return res if res != float("INF") else -1

        return find_coin(amount)

    # 第二种 带备忘录的递归
    def coinChange1(self, coins: List[int], amount: int) -> int:
        memo = {}

        def find_coin(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1

            res = float("INF")
            for i in coins:
                sub = find_coin(n - i)
                if sub == -1: continue
                res = min(res, 1 + sub)
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return find_coin(amount)

    # 第3种 迭代算法
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange1([1, 2, 5], 11))
    print(s.coinChange2([1, 2, 5], 11))
