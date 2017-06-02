__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/1
"""
    Description:
    https://onedrive.live_jinsky.com/edit.aspx?cid=b59928c2fc58d936&id=documents&resid=B59928C2FC58D936!215&app=OneNote&&wd=target%28%2F%2F%E5%AE%9E%E9%AA%8C%E6%A5%BC-Python-%E4%BC%9A%E5%91%98%E8%AF%BE%E7%A8%8B.one%7C58a906e4-acb6-4548-9f77-4e64d351a726%2F%E4%BD%BF%E7%94%A8Python3%20%E7%BC%96%E5%86%99%E7%B3%BB%E5%88%97%E5%AE%9E%E7%94%A8%E7%9A%84%E8%84%9A%E6%9C%AC%20-2%20-%E6%96%87%E6%9C%AC%E6%96%87%E4%BB%B6%E7%BC%96%E7%A0%81%E6%A3%80%E6%B5%8B%E4%B8%8E%E8%BD%AC%E6%8D%A2%20-%20%E5%AE%9E%E9%AA%8C%E6%A5%BC%7Cab4373cf-7963-4f12-b383-4da42c8a6a03%2F%29
        使用Python3 编写系列实用的脚本 -2 -文本文件编码检测与转换 -
        一、实验简介
是否遇到这些问题：想检测文本编码信息却没有办法；打开文本文件却发现中文乱码。这个实验教你编写一个 Python3 脚本来解决这些问题！
这个脚本不仅能批量检测文本文件的编码信息，还能批量转换到任意编码，再无乱码之忧。
在本实验中还会使用到 argparse 模块处理命令行参数，完成本实验后，argparse 模块将成为你的一把利器

"""
import sys
import os
import argparse
from chardet.universaldetector import UniversalDetector

"""
2.2.1. 使用 argparse 模块处理命令行参数
argparse 模块使得编写用户友好的命令行接口非常容易。程序只需定义好它要求的参数，然后 argparse 将负责如何从 sys.argv 中解析出这些参数。argparse 模块还会自动生成帮助和使用信息并且当用户赋给程序非法的参数时产生错误信息
使用 argparse 的第一步是创建一个 ArgumentParser 对象，ArgumentParser 对象会保存把命令行解析成 Python 数据类型所需要的所有信息


"""

parser = argparse.ArgumentParser(description='文本文件编码检测与转换')

parser.add_argument('filePaths',nargs ='+',help='检测或转换的文件路径')
parser.add_argument('-e', '--encoding', nargs = '?', const = 'UTF-8',
                    help = '''
                            目标编码。支持的编码有：
                            ASCII, (Default) UTF-8 (with or without a BOM), UTF-16 (with a BOM),
                            UTF-32 (with a BOM), Big5, GB2312/GB18030, EUC-TW, HZ-GB-2312, ISO-2022-CN, EUC-JP, SHIFT_JIS, ISO-2022-JP,
                            ISO-2022-KR, KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251, ISO-8859-2, windows-1250, EUC-KR,
                            ISO-8859-5, windows-1251, ISO-8859-1, windows-1252, ISO-8859-7, windows-1253, ISO-8859-8, windows-1255, TIS-620
                            ''')
parser.add_argument('-o', '--output',help = '输出目录')

"""
关于方法 add_argument() 的使用，可参考下面的引用（限于篇幅只引用部分，
更多请查看官方文档: https://docs.python.org/3/library/argparse.html）.
上面这段代码代表着，我们的脚本将有 3 个命令行参数：指定源文件路径的必填参数；指定文件转换的目标编码的可选参数；
指定输出目录的可选参数

"""
# 解析参数，得到一个 Namespace 对象
args = parser.parse_args()
# 输出目录不为空即视为开启转换, 若未指定转换编码，则默认为 UTF-8
if args.output != None:
    if not args.encoding:
        # 默认使用编码 UTF-8
        args.encoding = 'UTF-8'
    # 检测用户提供的输出目录是否有效
    if not os.path.isdir(args.output):
        print('Invalid Directory: ' + args.output)
        sys.exit()
    else:
        if args.output[-1] != '/':
            args.output += '/'
# 实例化一个通用检测器
detector = UniversalDetector()
print()
print('Encoding (Confidence)',':','File path')

for filePath in args.filePaths:
    # 检测文件路径是否有效，无效则跳过
    if not os.path.isfile(filePath):
        print('Invalid Path: ' + filePath)
        continue
    # 重置检测器
    detector.reset()
    # 以二进制模式读取文件
    for each in open(filePath, 'rb'):
        # 检测器读取数据
        detector.feed(each)
        # 若检测完成则跳出循环
        if detector.done:
            break
    # 关闭检测器
    detector.close()
    # 读取结果
    charEncoding = detector.result['encoding']
    confidence = detector.result['confidence']
    # 读取结果
    if charEncoding is None:
        charEncoding = 'Unknown'
        confidence = 0.99
    print('{} {:>12} : {}'.format(charEncoding.rjust(8),
        '('+str(confidence*100)+'%)', filePath))
    if args.encoding and charEncoding != 'Unknown' and confidence > 0.6:
        # 若未设置输出目录则覆盖源文件
        outputPath = args.output + os.path.basename(filePath) if args.output else filePath
        with open(filePath, 'r', encoding = charEncoding, errors = 'replace') as f:
            temp = f.read()
        with open(outputPath, 'w', encoding = args.encoding, errors = 'replace') as f:
            f.write(temp)

if __name__ == '__main__':
    pass

