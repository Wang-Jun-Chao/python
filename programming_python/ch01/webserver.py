"""
用Python实现一个HTTP Web服务器，它知道如何运行服务器端CGI脚本，
从当前工作目录提供文件和脚本， Python脚本必须存储在webdir\cgi-bin或
webdiT\htbin 中，
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'  # 存放HTML文件和cgi-b扭脚本文件夹的所在
port = 80  # 缺省http://localhost/, 也可以使用http://localhost:xxxx/
os.chdir(webdir)  # 在HTML根目录中运行
srvraddr = ("", port)  # 我的主机名和端口号
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
