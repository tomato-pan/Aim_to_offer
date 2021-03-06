'''
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
实现 NumArray 类：

    NumArray(int[] nums) 使用数组 nums 初始化对象
    int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）
    范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
示例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

'''


class NumArray:

    # def __init__(self, nums: list):
    #     self.nums = nums
    #
    # def sumRange(self, i: int, j: int) -> int:
    #     if i < 0 or i > len(self.nums) or j < 0 or j > len(self.nums): return None
    #     return sum(self.nums[i:j + 1])

    def __init__(self, nums: list):
        self.sums = [0]
        for i in nums:
                self.sums.append(self.sums[-1]+i)
        print(self.sums)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1]-self.sums[i]

if __name__ == '__main__':
    num = NumArray([-2, 0, 3, -5, 2, -1])
    print(num.sumRange(0, 2))
    print(num.sumRange(2, 5))
    print(num.sumRange(0, 5))
