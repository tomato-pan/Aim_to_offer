class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def find_max(self,root):
        res = []
        depth = 1
        def find_max1( root,depth):
            if root is None:return 0
            if root.left==None and root.right == None:
                res.append(depth)
            find_max1(root.left,depth+1)
            find_max1(root.right,depth+1)
        find_max1(root,depth)
        return max(res)

    def find_depth(self,root):
        if root is None: return 0
        left_d = self.find_depth(root.left)
        right_d = self.find_depth(root.right)
        return max(left_d,right_d)+1

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pass


if __name__ == '__main__':
    t = TreeNode(val=1)
    t.left = TreeNode(val=2)
    t.left.left = TreeNode(val=3)
    t.right = TreeNode(val=5)
    t.right.left = TreeNode(val=6)
    print(t.find_max(t))
    print(t.find_depth(t))