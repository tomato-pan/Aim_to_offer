def isPalindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1
    while left < right:
        if (string[left] != string[right]):
            return False
        left += 1
        right -= 1
    return True


# 链表的回文
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # @staticmethod
    # def traverse(head):
    #     if head is None: return
    #     ListNode.traverse(head.next)
    #     print(head.val)


class Solution:
    def isPalindrome1(self, head: ListNode) -> bool:
        global left
        left = head
        return self.traverse(head)

    def traverse(self, right):
        global left
        if right is None: return True
        res = self.traverse(right.next)
        res = res and (right.val == left.val)
        left = left.next
        # print(head.val)
        return res

    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head: ListNode):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        if not head: return True
        # 快慢指针寻找后半部分链表
        pre, slow, fast = None, head, head
        while fast and fast.next:
            slow = slow.next
            pre = slow
            fast = fast.next.next
        if fast:
            pre = slow
            slow = slow.next
        # 翻转后半部分
        q = right = reverse(slow)
        left = head
        while right and left:
            if left.val != right.val:
                pre.next = reverse(q)
                return False
            left = left.next
            right = right.next
        # 恢复链表
        pre.next = reverse(q)
        return True


if __name__ == '__main__':
    # print(isPalindrome("asdsa"))
    a = ListNode(val=1)
    a.next = ListNode(val=2)
    a.next.next = ListNode(val=3)
    a.next.next.next = ListNode(val=3)
    a.next.next.next.next = ListNode(val=2)
    a.next.next.next.next.next = ListNode(val=1)
    a.next.next.next.next.next.next = None
    print(Solution().isPalindrome(a))
