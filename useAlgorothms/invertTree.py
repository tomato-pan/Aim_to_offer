# LC226
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root: TreeNode) -> None:
        if root is None: return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def print_ord(self,root):
        r = root
        root_r = root.right
        while root is not None:
            print(root.val)
            root=root.left
            if root_r is not None:
                print(root_r.val)
                root_r=root_r.right





if __name__ == '__main__':
    root = TreeNode(val=4)
    root.left = TreeNode(val=2)
    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=3)
    root.right = TreeNode(val=7)
    root.right.left = TreeNode(val=6)
    root.right.right = TreeNode(val=9)
    solution = Solution()
    invert = solution.invertTree(root)
    solution.print_ord(invert)
    print(invert)
