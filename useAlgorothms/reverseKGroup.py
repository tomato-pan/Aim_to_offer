# LC25
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse(self, a: ListNode, b: ListNode):
        pre = None
        cur = a
        nxt = a
        while (cur != b):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        a = head
        b = head
        for i in range(k):
            if b is None: return head
            b = b.next
        newHead = self.reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return newHead


if __name__ == '__main__':
    a = ListNode(val=1)
    a.next = ListNode(val=2)
    a.next.next = ListNode(val=3)
    a.next.next.next = ListNode(val=4)
    a.next.next.next.next = ListNode(val=5)
    a.next.next.next.next.next = ListNode(val=6)
    a.next.next.next.next.next.next = None
    abc = Solution()
    abcd = abc.reverseKGroup(a,3)
    while abcd:
        print(abcd.val)
        abcd = abcd.next