# Problem: C - Consecutive
# Contest: Toyota Programming Contest 2023#7（AtCoder Beginner Contest 328）
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc328/tasks/abc328_c
# Memory Limit: 1024
# Time Limit: 2000
# Start: Wed 15 Jul 2026 05:23:44 PM

import sys, itertools

def main():
    [n,q] = [int(i) for i in input().split()]
    s = input()
    
    s_dupes = [0]
    for i in range(1,len(s)):
        if s[i] == s[i-1]: # when s[i] == s[i-1] we have "seen" another pair
            s_dupes.append(1)
        else:
            s_dupes.append(0)

    s_dupes = list(itertools.accumulate(s_dupes)) # convert to accumulation ; how many have we seen so far
    # why does this work over simply whether or not we see one at that point?
    # because:
    # we can't keep track of if one is the edge/end of one, but we can if we "carry" it foward by accumulating
    # print([c for c in s])
    # print(s_dupes)

    queries = []
    for q in sys.stdin:
        queries.append([int(i) for i in q.split()])
    for q in queries:
        print(s_dupes[q[1]-1] - s_dupes[q[0]-1])
    


if __name__ == '__main__':
    main()
