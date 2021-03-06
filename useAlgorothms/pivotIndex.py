# LC724

class Solution:
    def pivotIndex(self, nums) -> int:
        sum_all = sum(nums)
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum_all - left - nums[i]
            print(left, right)
            if left == right: return i
        return -1

    def pivotIndex1(self, nums) -> int:
        sum_all = sum(nums)
        sum1 = 0
        for i in range(len(nums)):
            print(sum1, nums[i],sum_all)
            if 2 * sum1 + nums[i] == sum_all: return i
            sum1+=nums[i]
        return -1


if __name__ == '__main__':
    so = Solution()
    print(so.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(so.pivotIndex1([1, 7, 3, 6, 5, 6]))
