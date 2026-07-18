# Problem: Apple Division
# Contest: CSES Problem Set
# Judge: CSES
# URL: https://cses.fi/problemset/task/1623
# Memory Limit: 512
# Time Limit: 1000
# Start: Fri 17 Jul 2026 10:12:26 PM


def main():
    n: int = int(input())
    w: list[int] = list(map(int, input().split()))
    
    ans = float('inf')
    for mask in range(1 << (n-1)):
        sum1 = 0
        sum2 = 0
        for i in range(n):
            if (mask & (1 << i)):
                sum1 += w[i]
            else:
                sum2 += w[i]
        ans = min(abs(sum1 - sum2), ans)
    print(ans)
if __name__ == '__main__':
    main()
