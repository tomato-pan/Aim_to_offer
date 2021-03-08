# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):
        if root is None: return []
        res = []

        def postorder(root, res):
            if root.left:
                postorder(root.left, res)
            if root.right:
                postorder(root.right, res)
            res.append(root.val)

        postorder(root, res)
        return res

    def levelOrder(self, root: TreeNode) -> list:
        res = []
        if root:
            self.lever(root, res)
            return res
        else:
            return res

    def lever(self, root, res):
        queue = [root]
        while queue:
            res_lever = []
            for i in range(len(queue)):
                cur_node = queue.pop(0)
                res_lever.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(res_lever)
#DFS
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root:
    #         self.DFS(root, 1, res)
    #         return res
    #     else:
    #         return res
    #
    # def DFS(self, root, level, res):
    #     if len(res) < level:
    #         res.append([])
    #     res[level - 1].append(root.val)
    #     if root.left:
    #         self.DFS(root.left, level + 1, res)
    #     if root.right:
    #         self.DFS(root.right, level + 1, res)

if __name__ == '__main__':
    root = TreeNode(val=1)
    root.left = None
    root.right = TreeNode(val=2)
    root.right.left = TreeNode(val=3)
    root.right.right = None
    ss = Solution()
    print(ss.levelOrder(root))
