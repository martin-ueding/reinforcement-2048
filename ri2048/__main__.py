#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import game


def main(options):
    board = game.Game()
    print('Init:')
    print(board)
    for direction in game.directions:
        board.move(direction)
        print(f'Move {direction.name}:')
        print(board)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    options = parser.parse_args()
    main(options)
