#!/usr/bin/env python3

from engine import Engine
from argparse import ArgumentParser
import sys


class TermClient(Engine):

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
        super().__init__(argument.file, argument.lect)

    def display(self, obj):
        for data in obj: print(data)

    def command(self, cmd):
        if cmd == "h":
            return ' i \t\t\t\t info for word hints \n'\
            ' c <tar> <in> \t\t\t change target lang (german,pinyin,hanyu) \n'\
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
            print("\n ratio: {}%".format(int(self.stats()*100)))
            sys.exit()
        else:
            return "not a command"

    def execute(self):
        sys.stdout.write("\033[0;0m")               # reset coloring
        msg = input(self.load())
        if len(msg) == 1:
            out = self.command(msg)
        else:
            out = self.eval(msg)
        if out == "correct":
            sys.stdout.write("\033[0;32m")
            print(out)
        elif out == "false":
            sys.stdout.write("\033[1;31m")
            print(out)
        else:
            sys.stdout.write("\033[0;0m")
            print(out)


def main():
    client = TermClient()
    try:
        while True:
            client.execute()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
