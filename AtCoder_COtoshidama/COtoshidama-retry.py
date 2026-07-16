# Problem: C - Otoshidama
# Contest: AtCoder Beginner Contest 085
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc085/tasks/abc085_c
# Memory Limit: 256
# Time Limit: 2000
# Start: Tue 14 Jul 2026 01:55:19 PM

import sys

def main():
    max_bills, goal_total = map(int, input().split())
    v3, v2, v1 = 1000, 5000, 10000
    for b1 in range(max_bills + 1):
        for b2 in range(max_bills + 1 - b1):
            b3 = max_bills - b1 - b2
            if b1*v1 + b2*v2 + b3*v3 == goal_total: 
                print(f"{b1} {b2} {b3}")
                return
    print("-1 -1 -1")


if __name__ == '__main__':
    main()
