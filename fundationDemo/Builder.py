from abc import ABCMeta, abstractmethod


class Builder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass


class Thin(Builder):
    def draw_left_arm(self):
        print("画左手！")


class Director(object):
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()


if __name__ == '__main__':
    thin = Thin()
    director = Director(thin)
    director.draw()
