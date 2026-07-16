# Problem: B - 1122 String
# Contest: AtCoder Beginner Contest 381
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc381/tasks/abc381_b
# Memory Limit: 1024
# Time Limit: 2000
# Start: Tue 14 Jul 2026 04:30:17 PM

import sys

def main():
    s = input()
    if len(s) % 2 != 0:
        print("No")
        return
    seen = set()
    for c in range(0, len(s), 2):
        if s[c] != s[c+1] or s[c] in seen:
            print("No")
            return
        else:
            seen.add(s[c])
    print("Yes")


if __name__ == '__main__':
    main()
