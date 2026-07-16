# Proiblem: C - Otoshidama
# Contest: AtCoder Beginner Contest 085
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc085/tasks/abc085_c
# Memory Limit: 256
# Time Limit: 2000
# Start: Mon 13 Jul 2026 07:29:45 PM

import sys

val_bill1 = 10000
val_bill2 = 5000
val_bill3 = 1000
memo: dict[tuple[int, int, int, int, int], tuple[int, int, int, int, int]] = dict()

# INPUT: an array of arrays --> [ [1,2,3], [4,5,6] ]
# OUTPUT: the maximum value 3-value array --> given all will have same max_bills, we can also just pick the first with pos value
def max_of_arrays(arrays:list[list[int]]) -> list[int]:
    sum_arrays = [1 if sum(i) > 0 else 0 for i in arrays]
    if sum(sum_arrays) > 0:
        return arrays[sum_arrays.index(1)]
    else:
        return arrays[0]
    
def helper(n_bill1: int, n_bill2: int, n_bill3: int, goal_total: int, max_bills: int) -> list[int]:
    global memo, val_bill1, val_bill2, val_bill3

    curr_total = val_bill1 * n_bill1 + val_bill2 * n_bill2 + val_bill3 + n_bill3
    curr_bills = n_bill1 + n_bill2 + n_bill3

    if (n_bill1, n_bill2, n_bill3, goal_total, max_bills) in memo:
        return list(memo[(n_bill1, n_bill2, n_bill3, goal_total, max_bills)])

    # print(n_bill1, n_bill2, n_bill3)

    output: tuple[int,int,int,int,int] = (-2, -2, -2, -2, -2)
    if goal_total == 0 and curr_bills == max_bills: 
        output = (n_bill1, n_bill2, n_bill3, goal_total, max_bills)
    elif goal_total == 0 and curr_bills != max_bills:
        output = (-1, -1, -1, -1, -1)
    elif goal_total < 0:
        output = (-1, -1, -1, -1, -1)
    # now we have goal_total > 0
    elif curr_bills > max_bills:
        output = (-1, -1, -1, -1, -1)
    else:
        output = tuple(max_of_arrays( [helper( n_bill1 + 1, n_bill2,     n_bill3,     goal_total-val_bill1, max_bills), 
                                       helper( n_bill1,     n_bill2 + 1, n_bill3,     goal_total-val_bill2, max_bills), 
                                       helper( n_bill1,     n_bill2,     n_bill3 + 1, goal_total-val_bill3, max_bills)] ))

    # print(n_bill1, n_bill2, n_bill3, goal_total, max_bills)
    # print(output, '\n\n')

    memo[(n_bill1, n_bill2, n_bill3, goal_total, max_bills)] = output
    return list(memo[(n_bill1, n_bill2, n_bill3, goal_total, max_bills)])[:3]

def main():
    [max_bills, goal_total] = [int(i) for i in sys.stdin.readline().split()]

    # if goal_total == 0 && curr_bills == max_bills: success
    # elif goal_total == 0 and curr_bills != max_bills: fail
    # if goal_total < 0: fail
    # if curr_bills > max_bills: fail 

    out = ""
    for i in helper(0,0,0,goal_total, max_bills):
        out += str(i) + " "
    print(out[:-1])


if __name__ == '__main__':
    main()
