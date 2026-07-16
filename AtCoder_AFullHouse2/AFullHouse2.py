# Problem: A - Full House 2
# Contest: AtCoder Beginner Contest 386
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc386/tasks/abc386_a
# Memory Limit: 1024
# Time Limit: 2000
# Start: Tue 14 Jul 2026 02:29:53 PM

import sys

def main():
    arr = list(map(int, input().split()))
    # 3, 1 
    # 2, 2 
    freq = dict()
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1 
    if list(freq.values()).count(2) == 2: print("Yes")
    elif 3 in list(freq.values()) and 1 in list(freq.values()): print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
