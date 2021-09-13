from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

if __name__ == '__main__':
    s = Solution()
    print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))
    print(s.rotate(nums = [-1,-100,3,99], k = 2))