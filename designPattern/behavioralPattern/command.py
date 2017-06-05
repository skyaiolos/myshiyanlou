__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/5
"""
    Description:
        四、命令模式(Command)
顾名思义，命令模式就是对命令的封装。所谓封装命令，就是将一系列操作封装到命令类中，并且命令类只需要对外公开一个执行方法execute，
调用此命令的对象只需要执行命令的execute方法就可以完成所有的操作。这样调用此命令的对象就和命令具体操作之间解耦了。
更进一步，通过命令模式我们可以抽象出调用者，接收者和命令三个对象。调用者就是简单的调用命令，然后将命令发送给接收者，
而接收者则接收并执行命令，执行命令的方式也是简单的调用命令的execute方法就可以了。发送者与接收者之间没有直接引用关系，
发送请求的对象只需要知道如何发送请求，而不必知道如何完成请求。下面让我们使用 Python 来实现命令模式。

"""

import abc


class VmReceiver(object):
    """
    命令接收者，真正执行命令的地方
    """

    def start(self):
        print("Virtual machine start")

    def stop(self):
        print("Virtual machine stop")


class Command(object):
    """
    命令抽象类
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """
        命令对象对外只提供 execute 方法
        """
        pass


class StartVmCommand(Command):
    """
    开启虚拟机的命令
    """

    def __init__(self, recevier):
        """
        使用一个命令接收者初始化
        """
        self.recevier = recevier

    def execute(self):
        """
        真正执行命令的时候命令接收者开启虚拟机
        """
        self.recevier.start()


class StopVmCommand(Command):
    """
    停止虚拟机的命令
    """

    def __init__(self, recevier):
        """
        使用一个命令接收者初始化
        """
        self.recevier = recevier

    def execute(self):
        """
        真正执行命令的时候命令接收者关闭虚拟机
        """
        self.recevier.stop()


class ClientInvoker(object):
    """
    命令调用者
    """

    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    recevier = VmReceiver()
    start_command = StartVmCommand(recevier)
    # 命令调用者同时也是客户端，通过命令实例也执行真正的操作
    client = ClientInvoker(start_command)
    client.do()
    # 能告诉命令接收者执行不同的操作
    stop_command = StopVmCommand(recevier)
    client.command = stop_command
    client.do()
