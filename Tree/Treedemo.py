# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代
    def preorderTraversal(self, root: TreeNode):
        if not root :return []
        res = []
        stack = []
        node = root
        while stack or node:  # 顺序:根左右
            while node:
                res.append(node.val)
                print(node.val)
                stack.append(node)  # 记录当前节点
                node = node.left
            node = stack.pop()  # 当左节点遍历完，出栈
            node = node.right  # 开始遍历右节点
        return res

    # 递归
    def preorderTraversal1(self, root: TreeNode):
        list1 = []

        def preorder(root):
            if root is None: return
            list1.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return list1

    # 递归
    def inorderTraversal(self, root: TreeNode):
        res = []
        def inorder(root): # 顺序 左根右
            if root is None: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

    # 递归
    def inorderTraversal1(self, root: TreeNode):
        if not root: return []
        res = []
        stack = []
        node = root
        while stack or node:  # 顺序 左根右
            while node:
                res.append(node.val)
                print(node.val)
                stack.append(node)  # 记录当前节点
                node = node.left
            node = stack.pop()  # 当左节点遍历完，出栈
            node = node.right  # 开始遍历右节点
        return res
if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = None
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = None
    so = Solution()
    print(so.inorderTraversal(tree))
