"""
实现一个图形界面，用千查看和更新存储千shelve中的类实例，
该shelve保存在脚本运行的机器上，可能是一个或多个本地文件，
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text="Fetch", command=fetchRecord).pack(side=LEFT)
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]  # 使用建获取数据，井在GUI 中展示
    except:
        showerror(title='Error', message='No such key I')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]  # 更新已有记录
    else:
        from programming_python.ch01.person import Person  # 在该键值下生成／保存新记录
        record = Person(name='?', age='?')  # eval, 字符串必须用引号引起来
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record


db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()  # 程序退出或窗口关闭时， 程序执行将返回到这里
