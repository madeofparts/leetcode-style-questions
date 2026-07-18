# Problem: B - 105
# Contest: AtCoder Beginner Contest 106
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc106/tasks/abc106_b
# Memory Limit: 976
# Time Limit: 2000
# Start: Thu 16 Jul 2026 10:00:40 PM

import sys

def main():
    n = int(input())
    
    ans = 0

    # generate odd numbers in the range [1,n]
    for i in range(1,n+1,2):
        divisors = 0
        for j in range(1,i+1):
            if i % j == 0: divisors += 1
        if divisors == 8:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
