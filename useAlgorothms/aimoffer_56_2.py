class Solution:
    def singleNumber(self, nums) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i

    def singleNumber1(self, nums) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == '__main__':
    s = Solution()
    num = s.singleNumber1([3,4,3,3])
    print(num)