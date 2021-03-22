import time
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")

    def replaceSpace1(self, s: str) -> str:
        ss = ""
        for i in s:
            if i == " ":
                ss += "%20"
            else:
                ss += i
        return ss

    def reversePrint(self, head: ListNode) -> List[int]:
        a, res = [], []
        if not head: a.append(head.val)
        for i in range(0, len(a), -1):
            res.append(a[i])
        return res


if __name__ == '__main__':
    s = Solution()
    # t1 = time.time()
    # print(s.replaceSpace1("we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! we are happy! "))
    # print(time.time()-t1)
    t1 = ListNode(1)
    t1.next = ListNode(2)
    t1.next.next = ListNode(3)
    print(s.reversePrint(t1))
