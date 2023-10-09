#!/usr/bin/env python

import sys


def reduce(c1, c2, m1, m2, v1, v2):
    m = (c1 * m1 + c2 * m2) / (c1 + c2)
    v = (c1 * v1 + c2 * v2) / (c1 + c2) + c1 * c2 * (((m2 - m1) / (c1 + c2)) ** 2)

    return c1 + c2, m, v


def main():
    line1 = sys.stdin.readline().strip()
    sp, mp, vp = line1.split()
    sp = int(s)
    mp = float(m)
    vp = float(v)
    for line in sys.stdin:
        s, m, v = line.split()
        s = int(s)
        m = float(m)
        v = float(v)
        cp, mp, vp = reduce(cp, c, mp, m, vp, v)

    print(mp, vp)


if __name__ == "__main__":
    main()
