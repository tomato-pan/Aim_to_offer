# LC114
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        if root is None: return None
        self.flatten(root.left)
        self.flatten(root.right)
        # 1
        left = root.left
        right = root.right
        # 2
        root.left = None
        root.right = left
        #3
        p = root
        while(p.right is not None):
            p = p.right
        p.right = right

