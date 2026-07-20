# Problem: C - Switches
# Contest: AtCoder Beginner Contest 128
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc128/tasks/abc128_c
# Memory Limit: 1024
# Time Limit: 2000
# Start: Sat 18 Jul 2026 08:20:42 PM


def main():
    n,m = map(int, input().split())
    # n - # of switches 
    # m - # of bulbs
    switches_connected = []
    for i in range(m):
        switches_connected.append([int(i) for i in input().split()][1:])

    on_condition = [int(i) for i in input().split()]
    # bulb[i] is on when the number of switches is congruent to p mod 2
    
    ans = 0

    for mask in range(1<<n):
        curr_condition = [0]*m

        for b in range(m):                      # each bulb
            for s in switches_connected[b]:
                if mask & (1 << (s-1)):             # if the switch for the bulb is on:
                    curr_condition[b] += 1
        for i in range(m):                                           # instead of checking all at the end, can check each bulb in the prev. loop and flip a flag
            if (curr_condition[i] % 2) == on_condition[i]:
                curr_condition[i] = 1
            else:
                curr_condition[i] = 0 
        if sum(curr_condition) == m:
            ans += 1 

    print(ans)




if __name__ == '__main__':
    main()
