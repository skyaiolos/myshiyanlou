__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/5
"""
    Description:
        简单工厂模式(Simple Factory)
一说到能创建产品的工厂类，你最先想到的最简单的实现是什么呢？一个函数，
传入需要创建的产品类型，然后返回相应的产品就行了。是不是够简单？下面让我们来实现它。

"""

import random

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
        return "Basic Course"


class ProjectCourse(object):
    """
    项目课
    """

    def get_labs(self):
        return "project_course: labs"

    def __str__(self):
        return "Project Course"


class SimpleCourseFactory(object):
    @staticmethod
    def create_course(type):
        """ 简单工厂，用于创建课程"""
        if type == 'bc':
            return BasicCourse()
        elif type == 'pc':
            return ProjectCourse()


if __name__ == '__main__':
    t = random.choice(['bc', 'pc'])
    print(t)
    course = SimpleCourseFactory.create_course(t)
    print(course.get_labs())
