import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_num = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_num or x <= self.min_num[-1] :
            self.min_num.append(x)
        print(self.stack)
        print(self.min_num)

    def pop(self) -> None:
        if self.stack.pop() == self.min_num[-1]:
            self.min_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.push(-3)
    s.push(-4)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())
