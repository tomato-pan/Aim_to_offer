from queue import Queue
from threading import Thread

running = 1
# Object that signals shutdown
_sentinel = object()

# A thread that produces data
def producer(out_q):
    data = "aaa"
    while running:
        # Produce some data
        data=data + "a"
        print("发送："+data)
        out_q.put(data)
        if len(data)==10:break

    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        print("接收：{}".format(data))
        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
