#!/usr/bin/env python

import sys


def Map(prices) -> str:
    l = len(prices)
    m = sum(prices)/l
    s=0
    for i in prices:
        s=s+(i-m)*(i-m)
    return f'{l}\t{m}\t{s/(l-1)}'


def main():
    prices = []
    line = sys.stdin.readline().strip().split(",")[9]
    while line:
        prices += [int(line)]
        line = sys.stdin.readline().strip().split(",")[9]
	
    print(Map(prices))


if __name__ == "__main__":
    main()
