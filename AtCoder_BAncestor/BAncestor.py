# Problem: B - Ancestor
# Contest: LINE  Verda Programming Contest（AtCoder Beginner Contest 263）
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc263/tasks/abc263_b
# Memory Limit: 1024
# Time Limit: 2000
# Start: Wed 15 Jul 2026 05:06:55 PM

import sys

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    # length = n-1
    # runs from 2 to N 
    curr = n
    count = 0
    while curr != 1:
        curr = p[curr-2]
        count += 1
    print(count)


if __name__ == '__main__':
    main()
