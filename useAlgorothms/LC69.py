class Solution:
    def mySqrt(self, x: int) -> int:
        prev = 0
        res = x
        while int(prev) != int(res):
            prev = res
            res = (res + x / res) / 2
        return int(res)
    def x(self,s1,s2):
        if s2 not in s1:return-1
        else: return s1.index(s2)
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
    print(s.x("hello","ll"))