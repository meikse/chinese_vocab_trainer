#!/usr/bin/env python3

# import sys 

from tkinter import *
from argparse import ArgumentParser
from engine import Engine

class App(Tk, Engine):

    def __init__(self):

        parser = ArgumentParser(description = "my program description")
        parser.add_argument("-f", 
                            "--file",
                            help = "use this vocab file (default: ./vocab.csv)",
                            required = False,
                            default = "./vocab.csv")
        parser.add_argument("-l",
                            "--lect",
                            help = "choose lecture difficulty (e.g 1)",
                            default = "1")
        argument = parser.parse_args()
        Engine.__init__(self, argument.file, argument.lect)

        Tk.__init__(self)
        # Engine.__init__(self)

        # self.geometry('{}x{}'.format(600, 400))   
        # self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        # config
        font = "Calibri {}".format(30)
        lang= ['german', 'pinyin', 'hanyu']
        string = " ".join(map(str, lang))
        var = StringVar(value=string)

        # # row 1
        self.quest= Label(self, text="target", font = font)
        self.answer= Label(self, text="result", font = font)

        self.quest.grid(row=0, column=0)
        self.answer.grid(row=0, column=1)
        # row 2
        self.entry= Entry(self, font = font)
        self.entry.bind('<Key-Return>', self.check_result)
        self.button = Button(self, text="enter", font = font)
        self.button.bind('<Button>', self.check_result)

        self.entry.grid(row=1, column=0)
        self.button.grid(row=1, column=1)
        # row 3
        self.target=Listbox(self, listvariable = var)
        self.target.bind('<<ListboxSelect>>', self.check_target)
        self.target.grid(row=2, column=0)

        self.input=Listbox(self, listvariable = var)
        self.input.bind('<<ListboxSelect>>', self.check_input)
        self.input.grid(row=2, column=1)

        self.flag = True
        # inital load
        self.update_quest()

    def update_quest(self):
        self.load()         # get self.index
        self.quest.config(text=self.lecture[self.index][self.flag_q])

    def check_result(self, event):
        if self.flag:
            if self.entry.get() == "":
                self.answer.config(text="")
            else:
                string = self.eval(self.entry.get())
                if string == "correct":
                    self.answer.config(text=string, fg = "green")
                else:
                    self.answer.config(text=string, fg = "red")
            self.flag = False
        else:
            self.answer.config(text="", fg = "black")
            self.entry.delete(0, END)
            self.update_quest()
            self.flag = True

    def check_target(self, event):
        if self.target.curselection():
            index = int(self.target.curselection()[0])
            value = self.target.get(index)
            self.flag_q=value

    def check_input(self, event):
        if self.input.curselection():
            index = int(self.input.curselection()[0])
            value = self.input.get(index)
            self.flag_a=value


def main():
    trainer = App()
    trainer.mainloop()

if __name__ == "__main__":
    main()
