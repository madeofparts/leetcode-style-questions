# Problem: A. Digital Counter
# Contest: Codeforces Round 282 (Div. 2)
# Judge: Codeforces
# URL: https://codeforces.com/problemset/problem/495/A
# Memory Limit: 256
# Time Limit: 1000
# Start: Thu 16 Jul 2026 10:15:55 AM

import sys

def main():
    [a,b] = [int(i) for i in input()]
    good_digits = {
            0 : 2,
            1 : 7,
            2 : 2,
            3 : 3,
            4 : 3,
            5 : 4,
            6 : 2,
            7 : 5,
            8 : 1,
            9 : 2
            }
    print(good_digits[a] * good_digits[b])

if __name__ == '__main__':
    main()
