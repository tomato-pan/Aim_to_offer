import math
class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

    def climbStairs1(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        finb = math.pow((1+sqrt5)/2,n+1)- math.pow((1-sqrt5)/2,n+1)
        return int(finb/sqrt5)
    def islegal(self, name:str) -> str:

        return int(finb/sqrt5)
if __name__ == '__main__':

    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs1(2))
