from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def down_load(filename):
    print("start downloading pid:[%d]" % getpid())
    print("start downloading...%s" % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%sfinish download，use %d seconds" % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=down_load, args=("Python for beginner.pdf",))
    p1.start()
    p2 = Process(target=down_load, args=("JAVA for beginner.pdf",))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("used %.2f seconds" % (end - start))


if __name__ == '__main__':
    main()
