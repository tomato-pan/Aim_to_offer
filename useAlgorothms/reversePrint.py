# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 时间复杂度 2N--> O(N),空间 O(N)
    def reversePrint(self, head: ListNode) -> List[int]:
        a, res = [], []
        while head:
            a.append(head.val)
            head = head.next
        a.reverse()
        return a

    # 递归  时间空间还不如上述迭代？
    def reversePrint1(self, head: ListNode) -> List[int]:
        a = []
        def rever(root):
            if root:
                rever(root.next)
                a.append(root.val)
            else:
                return
        rever(head)
        return a


if __name__ == '__main__':
    t1 = ListNode(1)
    t1.next = ListNode(3)
    t1.next.next = ListNode(2)
    s = Solution()
    print(s.reversePrint1(t1))
