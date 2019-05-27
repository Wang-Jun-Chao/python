#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
实现用来查看和更新保存在shelve 中类实例的基千Web的界面，
shelve保存在服务器上（如果是本地机器的话，就是同一个机器）
"""

import cgi, shelve, sys, os  # cgi.test()转储输人

shelvename = 'class-shelve'  # shelve文件在当前工作目录
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()  # 解析表单数据
print('Content-type: text/html')  # 响应html中的hdr和空行
sys.path.insert(0, os.getcwd())  # 为了这个和pickler查找person

# 主html模板
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method="POST" action="peoplecgi.py">
    <table>
        <tr>
            <th>key</th>
            <td><input type="text" name="key" value="%(key)s"></td>
        </tr>
        $ROWS$
    </table>
    <p>
        <input type="submit" value="Fetch" name="action">
        <input type="submit" value="Update" name="action">
    </p>
</form>
</body>
</html>
"""

# 为$ROWS$的数据行插入html
rowhtml = """
<tr>
    <th>%s</th>
    <td><input type="text" name="%s"value="%%(%s)s"></td>
</tr>
\n
"""
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)


def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:                    # 值可能包含&, >等字符
        value = new[field]                      # 作为代码显示：被引号引起
        new[field] = cgi.escape(repr(value))  # 转义html字符
    return new


def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__  # 使用属性字典
        fields['key'] = key  # 填充响应字符串
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]  # 更新已有记录
        else:
            from programming_python.ch01.person import Person  # 为键值创建／保存新记录
            record = Person(name='?', age='?')  # eval, 字符串必须被引号引起
        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
print("action -> " + action)
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')  # 错误的提交按钮值
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))  # 使用dict来填充响应

