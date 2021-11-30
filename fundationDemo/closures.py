def print_msg(msg):
    def printer():
        print(msg)

    return printer()


"""装饰器：装饰器带参数"""


def my_decorator(name):
    def outer(func):
        def inner(*args, **kwargs):
            print("********")
            print("添加带装饰器参数%s的功能代码" % name)
            func(*args, **kwargs)

        return inner

    return outer


@my_decorator(name='settings')
def script3(arg):
    print("测试----%s" % arg)


"""基于类封装的带参数装饰器"""


class MyDecorator:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def inner(*args, **kwargs):
            print("********")
            print("添加带装饰器参数%s的功能代码" % self.name)
            func(*args, **kwargs)

        return inner


@MyDecorator(name="settings")
def script4(arg):
    print("测试----%s" % arg)


if __name__ == '__main__':
    print_msg("message!")
    script3("bbb")
    script4("ddd")
