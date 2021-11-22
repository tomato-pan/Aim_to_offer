from random import randint
from threading import Thread
from time import sleep, time


# 继承线程Thread类
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("start downloading...%s" % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("%sfinish download,use %d seconds" % (self._filename, time_to_download))


def main():
    start = time()
    p1 = DownloadTask("Python for beginner.pdf")
    p1.start()
    p2 = DownloadTask("JAVA for beginner.pdf")
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("used %.2f seconds" % (end - start))


if __name__ == '__main__':
    main()
