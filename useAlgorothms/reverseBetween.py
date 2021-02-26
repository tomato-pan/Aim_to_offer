# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


succ = None


class Solution:
    def reverse(self, head: ListNode, ) -> ListNode:
        if head.next is None: return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseOne(self, head: ListNode, one: int) -> ListNode:
        global succ
        if one == 1:
            succ = head.next
            return head
        # 以head.next为起点，反转前n-1个节点
        last = self.reverseOne(head.next, one - 1)
        head.next.next = head
        head.next = succ
        return last

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseOne(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head


if __name__ == '__main__':
    a = ListNode(val=1)
    a.next = ListNode(val=2)
    a.next.next = ListNode(val=3)
    a.next.next.next = ListNode(val=4)
    a.next.next.next.next = ListNode(val=5)
    a.next.next.next.next.next = None
    ss = Solution()
    last = ss.reverseBetween(a, 2,4)
    while last:
        print(last.val)
        last = last.next
