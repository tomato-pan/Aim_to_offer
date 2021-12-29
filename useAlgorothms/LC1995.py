from collections import defaultdict
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # 暴力遍历
        n = len(nums)
        count = 0
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(c + 1, n):
                    for d in range(d + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]: count += 1
        return count

    def countQuadruplets1(self, nums: List[int]) -> int:
        # 哈希表
        mp = defaultdict(int)
        n = len(nums)
        ans = 0
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                mp[nums[d] - nums[b + 1]] += 1
            for a in range(0, b):
                num = nums[a] + nums[b]
                if num in mp:
                    ans += mp[num]
        return ans

