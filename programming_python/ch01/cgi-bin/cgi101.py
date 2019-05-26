#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi

form = cgi.FieldStorage()  # 解析表单数据
print('Content-type: text/html\n')  # hdr加回车
print('<title>Reply Page</title>')  # html响应页面
if not 'user' in form:
    print('<hl>Who are you?</h1>')
else:
    print('<hl>Hello <i>%s</i>!</hl> ' % cgi.escape(form['user'].value))
