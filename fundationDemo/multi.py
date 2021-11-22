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


count = 0


def sub_task(string):
    global count
    # 各输出10，因为每个子进程有自己独立内部空间，都含有一个count变量
    while count<10:
        print(string,end=",",flush=True)
        count+=1
        sleep(0.1)

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
    # main()
    Process(target=sub_task,args=("ping",)).start()
    Process(target=sub_task,args=("pong",)).start()
