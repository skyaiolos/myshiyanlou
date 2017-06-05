__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/5
"""
    Description:
        工厂方法模式(Factory Method)
在简单工厂模式中，我们遇到了问题：如果需要增加一种课程，那我们需要修改工厂代码。
仔细想想，如果对工厂进行抽象化，让每个工厂只负责一种产品的生产，那这样当增加一种产品时，
就不需要修改已有的工厂了，只需要新增加一个工厂就行了，这样就避免修改整个工厂啦。让我们来实现它。

"""
import random
import abc

# 两种类型的课程
#     基础课程
#     项目课
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
#    Linux虚拟机
#    Mac OSX 虚拟机
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
