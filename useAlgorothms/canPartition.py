# LC416
class Solution(object):
    def canPartition(self, nums):
        s1 = sum(nums)
        if s1 % 2 != 0: return False
        s1 = int(s1 / 2)
        n = len(nums)
        dp = [[False for i in range(s1 + 1)] for j in range(n + 1)]
        for i in range(n): dp[i][0] = True
        for i in range(s1): dp[0][i] = False
        print(dp)
        for i in range(1, n + 1):
            for j in range(1, s1 + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        for i in dp:
            print(i)
        return dp[n][s1]

    def canPartition1(self, nums):
        s1 = sum(nums)
        if s1 % 2 != 0: return False
        s1 = s1 // 2
        n = len(nums)
        dp = [False for i in range(s1 + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(s1,-1,-1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        print(dp)
        return dp[s1]


if __name__ == '__main__':
    nums = [1,2,  5]
    ss = Solution()
    a = ss.canPartition1(nums)
    print(a)
