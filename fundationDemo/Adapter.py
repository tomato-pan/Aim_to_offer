# 结构型模型-适配器模型
class socket(object):
    def Trigle(self):
        print("power supply!")

class tableLamp:
    def needTwo(self): pass

class Adapter(tableLamp,socket):
    def needTwo(self):
        self.Trigle()
#这个是对象实现方式
class socket1(object):
    def Trigle(self):
        print ('power supply over')
#target
class tableLamp1(object):
    def needTwo(self):
        pass
#adapter
class Adapter1(tableLamp):
    def __init__(self,Socket):
        self.socket=Socket
    def needTwo(self):
        self.socket.Trigle()


if __name__ == '__main__':
    lamp = Adapter()
    lamp.needTwo()
    plug = socket1()
    lamp = Adapter1(plug)
    lamp.needTwo()

