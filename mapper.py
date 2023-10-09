#!/usr/bin/env python

import sys

def main():
    prices = []
    line = sys.stdin.readline().strip()
    while line:
        s+=1
	prices += [int(line)]
        line = sys.stdin.readline().strip()
    s = len(prices)
    m = sum(prices)/s
    v = 0
    for i in prices:
	v+=(i-m)**2
    v = v/(s-1)
    print(s, m, v)


if __name__ == "__main__":
    main()
