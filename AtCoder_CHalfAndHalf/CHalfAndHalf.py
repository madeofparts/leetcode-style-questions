# Problem: C - Half and Half
# Contest: AtCoder Beginner Contest 095
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc095/tasks/arc096_a
# Memory Limit: 256
# Time Limit: 2000
# Start: Thu 16 Jul 2026 10:18:15 PM

import sys

def main():
    a,b,c,x,y = map(int, input().split())
    # a - A-pizza price
    # b - B-pizza price
    # c - AB-pizza price
    
    # we need to prepare: x A-pizzas, y B-pizzas
    # if AB-pizzas are cheaper, we can use 2 to make 1 of each A-pizza and B-pizza
    # we can have more A-pizza or B-pizzas if we desire, as long as we fulfill X and Y
    
    # test 1: AB is cheaper
    # test 2: A,B individually is cheaper
    # test 3: AB, A 
    # test 4: AB, B 
    # test 5: AB, excess of A 
    # test 6: AB, excess of B
    cost = 0

    # first check 2*C vs. A+B --> determine if 2*AB is cheaper than A+B
    # also want to know 2*C vs. A and 2*C vs. B --> if 2*AB is cheaper than A or B

    if (2*c) < (a+b):
        while x > 0 and y > 0:
            cost += 2*c 
            x -= 1
            y -= 1

    if (2*c) < a and x > 0:
        while x > 0:
            cost += 2*c 
            x -= 1

    if (2*c) < b and y > 0:
        while y > 0:
            cost += 2*c 
            y -= 1

    while x > 0:
        cost += a
        x -= 1
    while y > 0:
        cost += b
        y -= 1
    print(cost)

if __name__ == '__main__':
    main()
