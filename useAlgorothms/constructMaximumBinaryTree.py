# LC654
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list) -> TreeNode:
        if not nums: return None
        # max_num = float("-inf")
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] > max_num:
        #         max_num = nums[i]
        #         index = i
        max_num = max(nums)
        index = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    a = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    aa =[3, 2, 1, 6, 0, 5]
    print(a)
    print(aa[:3])