# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


if __name__ == '__main__':
    t1 = TreeNode(val=3)
    t1.left = TreeNode(val=9)
    t1.right = TreeNode(val=20)
    t1.right.left = TreeNode(val=15)
    t1.right.right = TreeNode(val=7)
    s = Solution()
    print(s.maxDepth(t1))
