# -*- coding:utf-8 -*-
from tkinter import *
import tkinter as tk
from hwboard import Mouse
from PIL import Image, ImageTk
from gui import Recognition
from ImageUtils import changeImage28
import os


def creat_image():
    mn = Mouse()
    mn.create_image()


class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title('Mnist')
        w = Canvas(root, width=600, height=30)
        w.pack()

        Label(root, text='Welcome to the MNIST, please read the description below!').pack(side=TOP)
        Label(root, text='1.Choose the button1:Generate Pattern，press M to turn to the handwrite mode, press the mouse and move to draw the number pattern(between 0~9)').pack(side=TOP, anchor=W)
        Label(root, text='2.After finishing writing，press W to turn to the screenshot mode, press the mouse to choose the pattern, then press Q to quit and back to the list').pack(side=TOP, anchor=W)
        Label(root, text='3.Choose the button2:Refresh, to redisplay the pattern ').pack(side=TOP, anchor=W)
        Label(root, text='4.Choose the button3:Recognize，to recognize number(between 0~9)').pack(side=TOP, anchor=W)
        Label(root, text='The number is :').pack(side=TOP, anchor=CENTER)
        self.numLabel = Label(root, text='', relief=RAISED,fg="black", font=("黑体", 25, "bold"))
        self.numLabel.pack(side=TOP, anchor=CENTER)
        Label(root, text='').pack(side=TOP, anchor=W)

        fm = Frame(root)
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Button(fm, text='Generate Pattern', command=creat_image).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm, text='Refresh', command=self.changeImage).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm, text='Recognize', command=self.recognition).pack(side=TOP, anchor=W, fill=X, expand=YES)


        fm.pack(side=LEFT, fill=BOTH, expand=YES, padx=20)

        self.pilImage = Image.open("Num.png")
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label = Label(root, image=self.tkImage)
        self.label.pack()

        Label(root, text="Press the mouse and move to draw the number pattern").pack(side=BOTTOM)

    def changeImage(self):
        self.png = tk.PhotoImage(file="Num.png")
        self.label.configure(image=self.png)

    def recognition(self):
        base_dir = os.path.dirname(os.getcwd())
        re = Recognition(base_dir)
        img = Image.open('Num.png')
        img = changeImage28(img)
        results = re.readImage2result(rimg=img)
        self.numLabel.configure(text=str(results))


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
