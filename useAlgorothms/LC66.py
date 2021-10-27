from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        k = len(digits) - 1
        while k >= 0:
            digits[k] += 1
            digits[k] = digits[k]%10
            if digits[k] != 0:
                return digits
            k -= 1
        res = [0] * (n + 1)
        res[0] = 1
        return res

if __name__ == '__main__':
    s = Solution()
    aa =[0]
    print(s.plusOne(aa))
