__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/5
"""
    Description:
        抽象工厂模式(Abstract Factory)
在工厂方法模式中，我们会遇到一个问题，当产品非常多时，继续使用工厂方法模式会产生非常多的工厂类。
现在我们有一个产品是课程，但是仅仅依靠课程还没办法提供完美的服务，因为在 实验楼 你可以边学课程边做实验呢。
在哪里做实验呢？当然是在虚拟机里了。当然我们也有很多种虚拟机，比如 Linux 虚拟机和 Mac 虚拟机。
如果按照工厂方法模式的作法，我们需要创建 Linux 虚拟机工厂类和 Mac 虚拟机工厂类， 
这样我们就会有一堆工厂类了。但是在 实验楼 里，真正的情况是只有虚拟机和课程结合在一起才能给用户提供完美的服务。
我们就不能创建出一个能同时创建课程和虚拟机的工厂吗？因为我们知道其实用户的需求同时包含了课程和虚拟机，
如果有一座工厂能同时生产这两种产品就完美了。

"""

import random
import abc


# 两种类型的课程
class BasicCourse(object):
    """
    基础课程
    """

    def get_labs(self):
        return "basic_course: labs"

    def __str__(self):
        return "BasicCourse"


class ProjectCourse(object):
    """
    项目课
    """

    def get_labs(self):
        return "project_course: labs"

    def __str__(self):
        return "ProjectCourse"


# 两种类型的虚拟机
class LinuxVm(object):
    """
    Linux 虚拟机
    """

    def start(self):
        return "Linux vm running"


class MacVm(object):
    """
    Mac OSX 虚拟机
    """

    def start(self):
        return "Mac OSX vm running"


class Factory(object):
    """
    抽象工厂类, 现在工厂类不仅能创建课程，还能创建虚拟机了
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_course(self):
        pass

    @abc.abstractmethod
    def create_vm(self):
        pass


class BasciCourseLinuxFactory(Factory):
    """
    基础课程工厂类
    """

    def create_course(self):
        return BasicCourse()

    def create_vm(self):
        return LinuxVm()


class ProjectCourseMacFactory(Factory):
    """
    项目课程工厂类
    """

    def create_course(self):
        return ProjectCourse()

    def create_vm(self):
        return MacVm()
    

def get_factory():
    """
    随机获取一个工厂类
    """
    return random.choice([BasciCourseLinuxFactory, ProjectCourseMacFactory])()


if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    vm = factory.create_vm()
    print(course.get_labs())
    print(vm.start())
