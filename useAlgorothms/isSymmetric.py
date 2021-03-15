# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    # 递归
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        def is_mirror(t1, t2):
            if t1 is None and t2 is None: return True
            if t1 is None or t2 is None or t1.val != t2.val: return False
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
        return is_mirror(root.left,root.right)
    # 迭代
    def isSymmetric1(self, root: TreeNode) -> bool:
        if root is None: return True
        d = deque()
        d.appendleft(root.left)
        d.append(root.right)
        while d:
            left = d.popleft()
            right = d.pop()
            if not left and not right:continue
            if not left or not right or left.val != right.val:return False
            d.appendleft(left.right)
            d.appendleft(left.left)
            d.append(right.left)
            d.append(right.right)
        return True

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:return False
        if not root.left and not root.right:
            return root.val==targetSum
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)


if __name__ == '__main__':
    t1 = TreeNode(val=3)
    t1.left = TreeNode(val=1)
    t1.right = TreeNode(val=1)

    s = Solution()
    print(s.isSymmetric1(t1))
    print(s.hasPathSum(t1,3))