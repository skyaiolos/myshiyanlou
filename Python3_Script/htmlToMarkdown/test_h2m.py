__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/1
"""
    Description:
        
"""
import html2markdown

print(html2markdown.convert('<h2>Test</h2><pre><code>Here is some code</code></pre>'))
if __name__ == '__main__':
    pass
