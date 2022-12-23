#!/usr/bin/env python3

# order of .csv file : 
# | level | german | pinyin | hanyu | info

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
        self.index = self.correct = self.total = 0


    def forward(self):
        self.raw = csv.reader(open(self.file), delimiter=',')
        self.data = [data[:5] for data in self.raw]     # delete tail
        self.all_lectures = []
        for j in range(len(self.data)):              # convert list to dict
            # d = {keys[i]: lecture[j][i] for i in range(len(keys))}
            dict_row = map(lambda i: (self.keys[i], self.data[j][i]),
                           range(len(self.keys)))
            self.all_lectures.append(dict(dict_row))
        self.lecture = [row for row in self.all_lectures 
                        if row["level"] == self.level]


    def backward(self):
        new_list = [list(row.values()) for row in self.all_lectures]
        with open(self.file, 'w') as f:
            write = csv.writer(f)
            write.writerows(new_list)


    def load(self):
        comp = self.index
        while comp == self.index:           # not the same word again
            self.index = randint(0, len(self.lecture)-1)
        return "{}: ".format(self.lecture[self.index][self.flag_q])


    def eval(self, enter):
        self.total += 1
        if enter == self.lecture[self.index][self.flag_a]:
            self.correct += 1
            return "correct"
        else:
            return "false"

    def stats(self):
        return self.correct/self.total
