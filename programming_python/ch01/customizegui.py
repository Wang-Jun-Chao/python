from tkinter import mainloop
from tkinter.messagebox import showinfo
from programming_python.ch01.tkinter102 import MyGui


class CustomGui(MyGui):  # 继承init
    def reply(self):  # 替换reply
        showinfo(title='popup', message='Ouch!')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
