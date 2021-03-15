# Definition for a binary tree node.
# LC105 加深理解
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pOrder, iOrder):
            if not pOrder: return None
            root = TreeNode(pOrder[0])
            root_index = iOrder.index(root.val)
            root.left = helper(pOrder[1:root_index + 1], iOrder[0:root_index])
            root.right = helper(pOrder[root_index + 1:], iOrder[root_index + 1:])
            return root

        return helper(preorder, inorder)

        # if not preorder or not inorder:  # 递归终止条件
        #     return
        # root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        # idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # # 下面递归对root的左右子树求解即可
        # root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        # root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        # return root

        # 迭代？
    # 知道中序和后续，重建树
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(postorder[-1])  # 后续序为“左右根”，所以根据postorder最后位置可以确定root
        idx = inorder.index(postorder[-1])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root