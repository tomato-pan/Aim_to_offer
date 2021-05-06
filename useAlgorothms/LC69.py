class Solution:
    def mySqrt(self, x: int) -> int:
        prev = 0
        res = x
        while int(prev) != int(res):
            prev = res
            res = (res + x / res) / 2
        return int(res)

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))