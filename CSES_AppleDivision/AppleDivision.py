# Problem: Apple Division
# Contest: CSES Problem Set
# Judge: CSES
# URL: https://cses.fi/problemset/task/1623
# Memory Limit: 512
# Time Limit: 1000
# Start: Fri 17 Jul 2026 10:12:26 PM

import sys

def main():
    n = int(input())
    w = list(map(int, input().split()))

    min_diff = -1
    for i in range(2**(n-1)):
        s = [int(i) for i in f"{i:0{n}b}"]
        ones = 0
        zeros = 0
        for c in range(n):
            if s[c] == 1:
                ones += w[c]
            else:
                zeros += w[c]
        diff = ones - zeros
        diff = abs(diff)
        if min_diff == -1 or diff < min_diff:
            min_diff = diff

    print(min_diff)


if __name__ == '__main__':
    main()
