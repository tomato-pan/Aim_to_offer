# LC 116
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


class Solution(object):
    def connect(self, root):
        if root is None: return None
        self.connectTwo(root.left, root.right)
        return root
    def connectTwo(self, node1, node2):
        # connect two nodes
        if node1 is None or node2 is None: return
        node1.next = node2
        self.connectTwo(node1.left, node1.right)
        self.connectTwo(node2.left, node2.right)
        self.connectTwo(node1.right, node2.left)

    def connect2(self, root):
        if root is None: return None
        self.connectTwo(root.left, root.right)
        return root

if __name__ == '__main__':
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.left.left = TreeNode(val=4)
    root.left.right = TreeNode(val=5)
    root.right = TreeNode(val=3)
    root.right.left = None
    root.right.right = TreeNode(val=7)
    solution = Solution()
    invert = solution.connect(root)
    print(invert)

