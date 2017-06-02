__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/1
"""
    Description:
        https://docs.python.org/3/library/argparse.html
        The argparse module makes it easy to write user-friendly command-line interfaces. 
        The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages 
        and issues errors when users give the program invalid arguments.
        
        16.4.1. Example

"""

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print("\n-->Show info-- ")
print(args.accumulate(args.integers))
