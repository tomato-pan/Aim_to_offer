class Solution:
    def hammingWeight(self, n: int) -> int:
        sum1 = 0
        while n!=0:
            sum1+=1
            n = n&n-1
        return sum1
    def hammingWeight1(self, n: int) -> int:
        res = 0
        while n:
            res+=n&1
            n = n>>1
        return res

if __name__ == '__main__':
