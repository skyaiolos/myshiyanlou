__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/5
"""
    Description:
        单例模式(Singleton)
所谓单例模式，也就是说不管什么时候我们要确保只有一个对象实例存在。很多情况下，整个系统中只需要存在一个对象，
所有的信息都从这个对象获取，比如系统的配置对象，或者是线程池。这些场景下，就非常适合使用单例模式。
总结起来，就是说不管我们初始化一个对象多少次，真正干活的对象只会生成一次并且在首次生成。

单例模式的实现只需要找一个变量存放创建的实例，然后每次获取实例时，先检查变量中是否已保存实例，
如果没有则创建一个实例并将其存放到变量中，以后都从这个变量中获取实例就可以了。单例模式中，只会创建一次实例

"""


class Singleton:
    """
    单例类装饰器，可以用于想实现单例的任何类。注意，不能用于多线程环境。
    """

    def __init__(self, cls):
        """ 
        需要的参数是一个类 
        """
        self._cls = cls

    def Instance(self):
        """
        返回真正的实例
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


# 装饰器
@Singleton
class A:
    """一个需要单列模式的类"""

    def __init__(self):
        pass

    def display(self):
        return id(self)


if __name__ == '__main__':
    s1 = A.Instance()
    s2 = A.Instance()
    print(s1, s1.display())
    print(s2, s2.display())
    print(s1 is s2)
# <__main__.A object at 0x01481850> 21502032
# <__main__.A object at 0x01481850> 21502032
# True
