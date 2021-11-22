class Mercedes(object):
    """
    Benz
    """

    def __repr__(self):
        return "Mercedes-Benz"


class BMW(object):
    def __repr__(self):
        return "BMW"

class SimpleCarFactory(object):
    """简单工厂"""
    @staticmethod
    def product_car(name):
        if name == "mb":
            return Mercedes()
        elif name=="bmw":
            return BMW()


# 抽象工厂
class Mercedes_C63(object):
    def __repr__(self):
        return "Mercedes-Benz:C63"

class BMW_M3(object):
    """宝马 M3
    """
    def __repr__(self):
        return "BMW: M3"

#　两种SUV
class Mercedes_G63(object):
    """梅赛德斯 G63
    """
    def __repr__(self):
        return "Mercedes-Benz: G63"

class BMW_X5(object):
    """宝马 X5
    """
    def __repr__(self):
        return "BMW: X5"

class AbstractFactory(object):
    """抽象工厂
    可以生产小汽车外，还可以生产SUV
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass

    @abc.abstractmethod
    def product_suv(self):
        pass

class MercedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes_C63()

    def product_suv(self):
        return Mercedes_G63()

class BMWFactory(AbstractFactory):
    """宝马工厂
    """
    def product_car(self):
        return BMW_M3()

    def product_suv(self):
        return BMW_X5()

if __name__ == '__main__':
    mer = Mercedes()
    bmw = BMW()
    print(mer,bmw)
    c1= SimpleCarFactory.product_car("mb")
    c2 = SimpleCarFactory.product_car("bmw")
    print(c1, c2)
    b1 = MercedesFactory().product_car()
    b2 = BMWFactory().product_car()
    print(b1,b2)
    s1 = MercedesFactory().product_suv()
    s2 = BMWFactory().product_suv()
    print(s1, s2)