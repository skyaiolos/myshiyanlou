# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/1
import os, sys
from bs4 import BeautifulSoup
import markdown
import html5lib

"""Description:
    使用Python3 编写系列实用的脚本 -1 -Markdown to HTML 
    这个课程教授如何使用 Python 3 编写一个转换 markdown 为 HTML 的脚本文件，这个脚本能够进行批量处理操作，可以自定义 HTML 的 CSS 样式（默认没有样式），可以自定义输出目录（默认为 markdown 文件所在目录）
1.1. 知识点:

	• Python 3 的模块的安装
	• Python 3 基础知识
	• 使用 os 模块进行路径相关的操作
	• markdown 模块的使用
	• 使用 BeautifulSoup 模块格式化 HTML
	• 命令行选项的实现
	
    脚本文件支持 3 种命令行参数，分别是一个到多个 Markdown 文件路径，
    
    选项 -s 是 CSS 文件路径，选项 -o 是输出目录

"""


class MarkdownToHTML:
    """
    编写 MarkdownToHtml 类,有4个属性，3个方法属性，1个数据属性
    """
    # 因为 markdown 模块生成的 HTML 代码是不包括 head 标签的，这样会可能造成浏览器中渲染 HTML 时显示乱码，
    # 而且有时可能也需要添加 CSS 来美化网页, So 因为 markdown 模块生成的 HTML 代码是不包括 head 标签的，这样会可能造成浏览器中渲染 HTML 时显示乱码，而且我们有时可能也需要添加 CSS 来美化网页
    headTag = '<head><meta charset="utf-8" /></head>'

    def __init__(self, cssFilePath=None):
        '''构造方法，有一个参数, cssFilePath ，默认值为 None
        :param cssFilePath: The path of css file, default value : None
        '''
        if cssFilePath != None:
            self.genStyle(cssFilePath)

    def genStyle(self, cssFilePath):
        '''读取外部CSS文件的内容并存放到headTag变量中
        :param cssFilePath: The path of css file
        :return: 
        '''
        with open(cssFilePath, 'r', encoding='utf-8') as f:
            cssString = f.read()
        self.headTag = self.headTag[:-7] + f'<Style type="text/css">{cssString}</style>' \
                       + self.headTag[-7:]

    # def markdownToHtml(self, sourceFilePath, destinationDirectory=None, outputFileName=None):
    #     '''编译 Markdown 输出 HTM
    #     :param sourceFilePath: The path of source file
    #     :param destinationDirectory: The directory of destination
    #     :param outputFileName: The file name of output.
    #     :return:
    #     '''
    #     if not destinationDirectory:
    #         # 未定义输出目录则将源文件目录(注意要转换为绝对路径)作为输出目录
    #         destinationDirectory = os.path.dirname(os.path.abspath((sourceFilePath)))
    #
    #     if not outputFileName:
    #         # 未定义输出文件名则沿用输入文件名
    #         outputFileName = os.path.splitext(os.path.basename((sourceFilePath))[0] + '.html')
    #         # os.path.abspath()      # 将参数路径转为绝对路径并返回
    #         # os.path.dirname()      # 获得参数路径的目录部分并返回（如"\home\a.txt" 为参数，返回"\home"）
    #         # os.path.basename()     # 返回参数路径字符串中的完整文件名（文件名 + 后缀名）
    #         # os.path.splitext()     # 将参数转换为包含文件名和后缀名两个元素的元组并返回
    #         # For more ,refer to 官方文档 https://docs.python.org/3/library/os.html
    #
    #     # 输出文件的路径我们通过拼接 destinationDirectory，outputFileName 这两个变量中的字符串得到，
    #     # 若是变量 destinationDirectory 中的字符串并不以'/'字符结尾，那么输出文件的路径会是错误的，所以需要处理一下
    #     if destinationDirectory[-1] != '/':
    #         destinationDirectory += '/'
    #
    #     with open(sourceFilePath, 'r', encoding='utf-8') as f:
    #         markdownText = f.read()
    #
    #     rawHtml = self.headTag + markdown.markdown(markdownText, output_format='html5')
    #
    #     beautifyHtml = BeautifulSoup(rawHtml, 'html5lib').prettify()
    #     file_path = destinationDirectory + outputFileName
    #     with open(file_path, 'w', encoding='utf8') as f:
    #         f.write(beautifyHtml)

    def markdownToHtml(self, **arguments):
        if 'sourceFilePath' in arguments:
            sourceFilePath = arguments['sourceFilePath']
        else:
            return
        if 'destinationDirectory' in arguments:
            destinationDirectory = arguments['destinationDirectory']
        else:
            # 未定义输出目录则将源文件目录(注意要转换为绝对路径)作为输出目录
            destinationDirectory = os.path.dirname(os.path.abspath(sourceFilePath))
        if 'outputFileName' in arguments:
            outputFileName = arguments['outputFileName']

        else:
            # 未定义输出文件名则沿用输入文件名
            outputFileName = os.path.splitext(os.path.basename(sourceFilePath))[0] + '.html'
        if destinationDirectory[-1] != '/':
            destinationDirectory += '/'

        with open(sourceFilePath, 'r', encoding='utf-8') as f:
            markdownText = f.read()

        # 编译出原始 HTML 文本
        rawHtml = self.headTag + markdown.markdown(markdownText, output_format='html5')
        # 格式化 HTML 文本为可读性更强的格式
        beautifyHtml = BeautifulSoup(rawHtml, 'html5lib').prettify()
        file_path = destinationDirectory + outputFileName
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(beautifyHtml)


def main():
    mth = MarkdownToHTML()
    # 做一个命令行参数列表的浅拷贝，不包含脚本文件名
    argv = sys.argv[1:]
    # 目前列表 argv 可能包含源文件路径之外的元素（即选项信息）
    # 程序最后遍历列表 argv 进行编译 markdown 时，列表中的元素必须全部是源文件路径
    outputDirectory = None
    if '-s' in argv:
        cssArgIndex = argv.index('-s') + 1
        cssFilePath = argv[cssArgIndex]
        # 检测样式表文件路径是否有效
        if not os.path.isfile(cssFilePath):
            print('Invalid Path:' + cssFilePath)
            sys.exit()
        mth.genStyle(cssFilePath)
        # pop 顺序不能随意变化
        argv.pop(cssArgIndex)
        argv.pop(cssArgIndex - 1)

    if '-o' in argv:
        dirArgIndex = argv.index('-o') + 1
        outputDirectory = argv[dirArgIndex]
        # 检测输出目录是否有效
        if not os.path.isdir(outputDirectory):
            print('Invalid Directory: ' + outputDirectory)
            sys.exit()
        # pop 顺序不能随意变化
        argv.pop(dirArgIndex)
        argv.pop(dirArgIndex - 1)

        argumentsList = [dict([('sourceFilePath', filePath), ('destinationDirectory', outputDirectory)])
                         for filePath in argv]
    else:
        argumentsList = [dict([('sourceFilePath', filePath)]) for filePath in argv]
    # 至此，列表 argv 中的元素均是源文件路径
    # 遍历所有源文件路径
    for argument in argumentsList:
        # 判断文件路径是否有效
        if os.path.isfile(argument['sourceFilePath']):
            mth.markdownToHtml(**argument)
        else:
            print('Invalid Path:' + argument['sourceFilePath'])


if __name__ == '__main__':
    main()
