# Problem: Weird Algorithm
# Contest: CSES Problem Set
# Judge: CSES
# URL: https://cses.fi/problemset/task/1068
# Memory Limit: 512
# Time Limit: 1000
# Start: Tue 14 Jul 2026 02:41:40 PM

import sys

def main():
    n = int(input())
    out = f"{str(n)} "
    while n != 1:
        if n%2==0:
            n = int(n/2)
        else:
            n = 3*n + 1
        out += f"{str(n)} "
    print(out)

if __name__ == '__main__':
    main()
