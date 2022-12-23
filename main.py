#!/usr/bin/env python3

# import sys 

from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()

        self.geometry('{}x{}'.format(600, 400))   
        # self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # # row 1
        self.quest= Label(self, text="question")
        self.answer= Label(self, text="result")

        self.quest.grid(row=0, column=0, sticky="NSEW")
        self.answer.grid(row=0, column=1, sticky="NSEW")
        # row 2

        self.entry= Entry(self)
        self.button = Button(self, text="enter")

        self.entry.grid(row=1, column=1, sticky="NSEW")
        self.button.grid(row=1, column=2, sticky="NSEW"))
        # row 3
        self.german = Radiobutton(self, text="german")
        self.hanyu  = Radiobutton(self, text="hanyu")
        self.pinyin = Radiobutton(self, text="pinyin")

        self.german.grid(row=2, column=0, sticky="NSEW")
        self.hanyu.grid(row=2, column=1, sticky="NSEW")
        self.pinyin.grid(row=2, column=2, sticky="NSEW")


def main():
    trainer = App()
    trainer.mainloop()

if __name__ == "__main__":
    main()
