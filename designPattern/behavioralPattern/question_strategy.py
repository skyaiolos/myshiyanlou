__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/5
"""
    Description:
      二、策略模式(Strategy)
在实验楼问答模块中，一个问题可能有多种显示方式。如果用户有管理权限，那么问题的详情页面可能会显示编辑按钮，
如果是普通用户则只显示问题内容  
"""


class Question(object):
    """
    问题对象，没有使用策略模式之前的作法
    """

    def __init__(self, admin=True):
        self._admin = admin

    def show(self):
        """
        根据是否是管理员显示不同的信息 
        """
        if self._admin is True:
            return "show page with admin"
        else:
            return "show page with user"


if __name__ == '__main__':
    q = Question(admin=False)
    print(q.show())
