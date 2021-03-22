# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 时间复杂度 2N--> O(N),空间 O(N)
    def reversePrint(self, head: ListNode) -> List[int]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a[::-1]

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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = None
        while head:
            q = head  # 暂存后继节点至q存在head
            head = q.next  # 下一个节点
            q.next = p  # 修改next引用
            p = q
        head = p
        return head


if __name__ == '__main__':
    t1 = ListNode(1)
    t1.next = ListNode(3)
    t1.next.next = ListNode(2)
    s = Solution()
    print(s.reversePrint(t1))
