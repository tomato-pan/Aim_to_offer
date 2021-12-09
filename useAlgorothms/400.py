import time


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, n: int):
        t1 = time.time()
        self.func(self, n)
        print("耗时：{}".format(time.time() - t1))
        return self.func(self, n)


class Solution:
    @MyDecorator
    def findNthDigit(self, n: int) -> int:
        string = ""
        for i in range(1, n + 1):
            string += str(i)
        return int(string[n - 1])

    @MyDecorator
    def findNthDigit2(self, n: int) -> int:
        a, b = 1, 9
        while n > a * b:
            n -= a * b
            a += 1
            b *= 10
        return int(str((n - 1) // a + b // 9)[(n - 1) % a])


if __name__ == '__main__':
    ss = Solution()
    print(ss.findNthDigit2(100000000))
