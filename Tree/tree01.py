# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # 前序
    def preorder(self, root):
        if root == None: return
        print(root.val, end="->")
        self.preorder(root.left)
        self.preorder(root.right)
    # 中序
    def inorder(self, root):
        if root == None: return
        self.preorder(root.left)
        print(root.val, end="->")
        self.preorder(root.right)
    # 后序
    def postorder(self, root):
        if root == None: return
        self.preorder(root.left)
        self.preorder(root.right)
        print(root.val, end="->")
    # 层序遍历
    def BFS(self,root):
        if root == None:return
        queue = []
        queue.append(root)
        val = []
        while queue:
            currentNode = queue.pop(0)
            print(currentNode.val,end="->")
            val.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        print(val)
        return val

t = TreeNode(val=1)
t.left = TreeNode(val=2)
t.left.left = TreeNode(val=3)
t.right = TreeNode(val=5)
t.right.left = TreeNode(val=6)

t.preorder(t)
print()
t.inorder(t)
print()
t.postorder(t)
print()
t.BFS(t)