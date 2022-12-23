#!/usr/bin/env python3

# order of .csv file : 
# | level | german | pinyin | hanyu | info

import csv

class Client:

    def __init__(self):

        # parameter
        self.level = str(1) 
        self.flag = "german"                            # pinyin, hanyu
        self.file = "vocab.csv"
        self.keys = ["german","pinyin","hanyu","help"]
        # filter data
        self.raw = csv.reader(open(self.file), delimiter=',')
        self.data = [data[:5] for data in self.raw]     # delete tail
        self.lecture = [row[1:] for row in self.data    # clip to level
                        if row[0] == self.level]
        self.dictonary = []
        for j in range(len(self.lecture)):              # convert list to dict
            # d = {keys[i]: lecture[j][i] for i in range(len(keys))}
            dict_row = map(lambda i: (self.keys[i], self.lecture[j][i]),
                           range(len(self.keys)))
            self.dictonary.append(dict(dict_row))

    def display(self, obj):
        for data in obj: print(data)

    def parse(self):
        if self.flag == "pinyin":
            pass
        elif self.flag == "hanyu":
            pass
        else:
            pass

    def run(self):
        print("{}:")

    def save(self):
        pass
        

def main():
    client = Client()
    client.display(client.dictonary) 


if __name__ == "__main__":
    main()
