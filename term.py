#!/usr/bin/env python3

from engine import Engine


class TermClient(Engine):

    def __init__(self, level):
        super().__init__(level=level)


def main():
    client = TermClient(level = 1)
    while True:
        client.run()

if __name__ == '__main__':
    main()
