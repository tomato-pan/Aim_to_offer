# 全排列
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """itertools库内置了这个函数"""
        import itertools
        return itertools.permutations(nums)

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """自己写回溯法"""
        res = []
        def backtrack(nums, pre_list):
            if len(nums) <= 0:
                res.append(pre_list)
            else:
                for i in nums:
                    # 注意copy一份新的调用，否则无法正常循环
                    p_list = pre_list.copy()
                    p_list.append(i)
                    left_nums = nums.copy()
                    left_nums.remove(i)
                    backtrack(left_nums, p_list)
        backtrack(nums, [])
        return res

    def permute3(self, nums: List[int]) -> List[List[int]]:
        """回溯的另一种写法"""
        res = []
        length = len(nums)
        def backtrack(start=0):
            if start == length:
                # nums[:] 返回 nums 的一个副本，指向新的引用，这样后续的操作不会影响已经已知解
                res.append(nums[:])
            for i in range(start, length):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack()
        return res

if __name__ == '__main__':
    nums = [1,2,3,5]
    s = Solution()
    print(s.permute3(nums))
    print(s.permute2(nums))
    print(s.permute(nums))