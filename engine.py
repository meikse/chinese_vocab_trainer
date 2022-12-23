#!/usr/bin/env python3

# order of .csv file : 
# | level | german | pinyin | hanyu | info

import sys
import csv
from random import randint


class Engine:


    def __init__(self, file="./vocab.csv", level = 1):
        # vocab parameter
        self.level = str(level)
        self.flag_q = "german"                            # pinyin, hanyu
        self.flag_a = "pinyin"
        self.file = file
        self.keys = ["level","german","pinyin","hanyu","info"]
        # prep data
        self.forward()
        # initial parameter
        self.answered = False
        self.index = 0


    def forward(self):
        self.raw = csv.reader(open(self.file), delimiter=',')
        self.data = [data[:5] for data in self.raw]     # delete tail
        self.all_lectures = []
        for j in range(len(self.data)):              # convert list to dict
            # d = {keys[i]: lecture[j][i] for i in range(len(keys))}
            dict_row = map(lambda i: (self.keys[i], self.data[j][i]),
                           range(len(self.keys)))
            self.all_lectures.append(dict(dict_row))
        self.lecture = [row for row in self.all_lectures if row["level"] == self.level]


    def backward(self):
        new_list = [list(row.values()) for row in self.all_lectures]
        with open(self.file, 'w') as f:
            write = csv.writer(f)
            write.writerows(new_list)



    def load(self):
        if self.answered: 
            comp = self.index
            while comp == self.index:           # not the same word again
                self.index = randint(0, len(self.lecture)-1)
        return input("{}: ".format(self.lecture[self.index][self.flag_q]))


    def command(self, cmd):
            if cmd == "h":
                return ' i \t\t\t\t info for word hints \n'\
                ' c <lan> \t\t\t change target lang (german,pinyin,hanyu) \n'\
                ' n <ger> <pin> <han> <(inf)> \t new vocab for the list \n'\
                ' h \t\t\t\t for this help \n'\
                ' q \t\t\t\t quit this client'
            elif cmd == "i":
                return self.lecture[self.index][self.keys[-1]]
            elif cmd == "c":
                self.flag_q = input("target language: ")
                self.flag_a = input("input language: ")
            elif cmd == "n":
                new_entry = {self.keys[i]: input(self.keys[i] + ": ") 
                    for i in range(len(self.keys))}
                self.all_lectures.append(new_entry) # safe for this session
                self.backward()                     # safe in the file
            elif cmd == "q":
                sys.exit()
            else:
                return "not a command"


    def run(self):
        enter = self.load()
        # check for commands
        if len(enter) == 1:
            return self.command(enter)
        # check results
        else:
            if enter == self.lecture[self.index][self.flag_a]:
                return "correct"
            else:
                return "false"


# def main():
#     client = Engine()
#     while True:
#         client.run() 
    

# if __name__ == "__main__":
#     main()
