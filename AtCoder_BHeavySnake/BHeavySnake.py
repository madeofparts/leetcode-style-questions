# Problem: B - Heavy Snake
# Contest: HHKB Programming Contest 2025(AtCoder Beginner Contest 388)
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc388/tasks/abc388_b
# Memory Limit: 1024
# Time Limit: 2000
# Start: Tue 14 Jul 2026 02:52:51 PM

import sys

def main():
    [n,d] = list(map(int, input().split()))
    init = []
    curr = []
    for line in sys.stdin:
        line = [int(i) for i in line.split()]
        init.append(line)
        curr.append(line[0] * line[1])

    for i in range(d):
        for x in range(n):
            curr[x] += init[x][0]
        print(max(curr))

if __name__ == '__main__':
    main()
