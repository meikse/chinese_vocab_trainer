#!/usr/bin/env python3

from engine import Engine
import sys


class TermClient(Engine):

    def __init__(self, level):
        super().__init__(level=level)

    def display(self, obj):
        for data in obj: print(data)

    def execute(self):
        sys.stdout.write("\033[0;0m")               # reset coloring
        out = self.run()
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
    client = TermClient(level = 1)
    while True:
        client.execute()

if __name__ == '__main__':
    main()
