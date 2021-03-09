# LC33
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search1(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(s.search1(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(s.search1(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(s.search1(nums=[4, 5, 6, 7, 10, 20, 0, 1, 2], target=20))
    print(s.search(nums=[4, 5, 6, 7, 10, 20, 0, 1, 2], target=20))
