# Problem: B - Geometric Sequence
# Contest: AtCoder Beginner Contest 390
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc390/tasks/abc390_b
# Memory Limit: 1024
# Time Limit: 2000
# Start: Tue 14 Jul 2026 04:16:21 PM

import sys

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    for i in range(2,len(arr)):
        if arr[i-1]**2 != arr[i-2]*arr[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()
