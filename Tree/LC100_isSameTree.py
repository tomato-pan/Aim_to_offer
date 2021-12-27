# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)

    def check(self, p: TreeNode, q: TreeNode):
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)

if __name__ == '__main__':
    s = Solution()
    t = TreeNode(val=1)
    t.left = TreeNode(val=2)
    t.left.left = TreeNode(val=3)
    t.right = TreeNode(val=5)
    t.right.left = TreeNode(val=6)
    print(s.isSymmetric(t))
