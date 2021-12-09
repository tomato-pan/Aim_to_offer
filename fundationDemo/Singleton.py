class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton,"_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

from functools import wraps
from threading import RLock


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class chairMan(object):
    pass

if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1,obj2)
    cm1=chairMan()
    cm2=chairMan()
    print(cm1,cm2)