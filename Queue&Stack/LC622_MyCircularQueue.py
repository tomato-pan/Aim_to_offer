class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        # the capacity of queue
        self.k = k
        # the head of the queue
        self.front = 0
        # the rear of the queue
        self.rear = -1
        # the real length of the queue
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.length < self.k:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            self.length += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.length > 0:
            self.front = (self.front + 1) % self.k
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        if self.length > 0:
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if self.length > 0:
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.length == self.k:
            return True
        return False
    '''
    def __init__(self, k: int):
        self.capacity = k + 1
        self.queue = [0 for _ in range(self.capacity)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.rear - 1 + self.capacity) % self.capacity]
        return -1

    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.capacity == self.front:
            return True
        return False
    '''


if __name__ == '__main__':
    circularQueue = MyCircularQueue(8)
    print(circularQueue.enQueue(3))
    print(circularQueue.enQueue(9))
    print(circularQueue.enQueue(5))
    print(circularQueue.enQueue(0))
    print(circularQueue.queue)
    print(circularQueue.deQueue())
    print(circularQueue.deQueue())
    print(circularQueue.queue)
    print(circularQueue.isEmpty())
    print(circularQueue.isEmpty())
    print(circularQueue.Rear())
    print(circularQueue.Rear())
    print(circularQueue.deQueue())
    print(circularQueue.queue)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
