# Problem: Distinct Numbers
# Contest: CSES Problem Set
# Judge: CSES
# URL: https://cses.fi/problemset/task/1621
# Memory Limit: 512
# Time Limit: 1000
# Start: Mon 13 Jul 2026 06:13:59 PM

import sys

def main():
    # num_values = int(sys.stdin.readline())
    # values = {int(i) for i in sys.stdin.readline().split()}
    # print(len(values))
    values = [int(i) for i in sys.stdin.read().split()[1:]]
    values.sort()
    
    distincts = 0
    for i in range(len(values)):
        if (i == 0): 
            distincts += 1
        elif (values[i] != values[i-1]):
            distincts += 1
    print(distincts)

if __name__ == '__main__':
    main()
