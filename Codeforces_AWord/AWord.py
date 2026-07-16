# Problem: A. Word
# Contest: Codeforces Beta Round 55 (Div. 2)
# Judge: Codeforces
# URL: https://codeforces.com/problemset/problem/59/A
# Memory Limit: 256
# Time Limit: 2000
# Start: Tue 14 Jul 2026 04:07:11 PM

import sys

def main():
    s = str(input())
    if (2*sum(1 for i in s if i.isupper()) > len(s)):
        print(s.upper())
    else:
        print(s.lower())

if __name__ == '__main__':
    main()
