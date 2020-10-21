import random as r


# 在类的方法定义时，首个参数均为self
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1

        print("我向西游，现在位置", self.x, self.y)


class Goldfish(Fish):
    def __init__(self):
        # 子类会覆盖掉父类的同名的方法和属性，而且还不会自动调用
        # Fish.__init__(self)
        # 调用未绑定的父类方法
        # 使用super函数
        super().__init__()
        # 可以解决多继承问题，无论继承了多少个，都依次输出
        self.hung = True

    def eat(self):
        if self.hung:
            print("饿了要吃肉")
            self.hung = False;
        else:

            print("饱了不吃肉")


g = Goldfish()


class Hjfish():
    def __init__(self):
        super().__init__()


g.eat()
g.move()
