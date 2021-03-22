"""
# Definition for a Node.

"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        Mydic = dict()

        def recursion(node: 'Node') -> 'Node':
            if node is None: return None
            if node in Mydic: return Mydic.get(node)
            root = Node(node.val)
            Mydic[node] = root
            root.next = recursion(node.next)
            root.random = recursion(node.random)
            return root

        return recursion(head)
