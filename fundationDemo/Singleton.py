class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton,"_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance
if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1,obj2)
    import hashlib
    a="111"
