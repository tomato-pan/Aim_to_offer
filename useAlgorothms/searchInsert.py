"""
输入: [1,3,5,6], 5
输出: 2

输入: [1,3,5,6], 2
输出: 1

输入: [1,3,5,6], 7
输出: 4

输入: [1,3,5,6], 0
输出: 0

"""


# 排序数组-->二分法
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
            return len(nums)

    def searchInsert1(self, nums: list, target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi :
            mid = int((lo + hi) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi -=1
            else:
                lo +=1
        return lo


if __name__ == '__main__':
    so = Solution()
    print(so.searchInsert([1, 3, 5, 6], 5))
    print(so.searchInsert([1, 3, 5, 6], 2))
    print(so.searchInsert([1, 3, 5, 6], 7))
    print(so.searchInsert([1, 3, 5, 6], 0))
    print(so.searchInsert1([1, 3, 5, 6], 5))
    print(so.searchInsert1([1, 3, 5, 6], 2))
    print(so.searchInsert1([1, 3, 5, 6], 7))
    print(so.searchInsert1([1, 3, 5, 6], 0))
    print(so.searchInsert1([1], 0))
