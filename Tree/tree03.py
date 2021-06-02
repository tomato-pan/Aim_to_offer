# 二叉树的遍历
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        list_root = []

        def preorder(root):
            if root == None: return
            list_root.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return list_root

    # 中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list_root = []

        def inorder(root):
            if root == None: return
            inorder(root.left)
            list_root.append(root.val)
            inorder(root.right)

        inorder(root)
        return list_root

    # 后序遍历
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        list_root = []

        def postorder(root):
            if root == None: return
            postorder(root.left)
            postorder(root.right)
            list_root.append(root.val)

        postorder(root)
        return list_root

    # 层序遍历
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root == None: return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                current = queue.pop(0)
                tmp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.append(tmp)
        return res


if __name__ == '__main__':
    t = TreeNode(val=1)
    t.left = TreeNode(val=2)
    t.left.left = TreeNode(val=3)
    t.right = TreeNode(val=5)
    t.right.left = TreeNode(val=6)
    s = Solution()
    print(s.preorderTraversal(t))
    print(s.inorderTraversal(t))
    print(s.levelOrder(t))
