#!/usr/bin/env python3

from engine import Engine


class TermClient(Engine):

    def __init__(self, level):
        super().__init__(level=level)

    def display(self, obj):
        for data in obj: print(data)

    def execute(self):
        self.run()


def main():
    client = TermClient(level = 1)
    while True:
        client.execute()

if __name__ == '__main__':
    main()
