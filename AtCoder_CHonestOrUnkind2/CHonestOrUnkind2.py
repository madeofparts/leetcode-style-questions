# Problem: C - HonestOrUnkind2
# Contest: AtCoder Beginner Contest 147
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc147/tasks/abc147_c
# Memory Limit: 1024
# Time Limit: 2000
# Start: Fri 17 Jul 2026 02:55:08 PM

import sys

# 1 person, no confessions

# 2 people, both kind
# 2 people, both unkind --> not possible
# 2 people, one of each
# 2 people, uneven confession count

# 3 people 
# 1 - 2,1 3,1
# 2 - 3,0 1,1
# 3 - 2,0 1,1


def main():
    n = int(input()) # number of people, 1 through N 
    people: list[list[int | list[int]]] = []
    for _ in range(n):
        arr: list[int | list[int]] = []
        arr.append(int(input()))
        for _ in range(arr[0]):
            arr.append(list(map(int,input().split())))
        people.append(arr)

    ans = 0
    for mask in range(1<<n):                        # each state mask
        state = mask
        flag = True
        
#        print("\n ==for mask", mask, f" / {mask:0{n}b}==")
        for i in range(n):                          # mask individual bits --> "honest" people
            if not flag:
                break

            if mask & (1 << i):
                for j in range(people[i][0]):       # for each person who is honest, iterate through their confessions
                    suspect, kind = people[i][j+1]
                    
#                    print("before:", f"{state:05b}")
                    
                    if not state & (1 << i):                # assumed kind, someone else confessed they were unkind before we got to them
#                        print("Contradiction1")
                        flag = False

                    if kind:
                        state = state | (1 << (suspect - 1)) 
#                        print(f"{suspect} kind")

                    if not kind:   
#                        print(f"{suspect} unkind")
                        if mask & (1 << (suspect - 1)):
                            flag = False
#                            print("Contradiction3")
                        if ~state & (1 << (suspect - 1)):     # if a confessed-to-be unkind person is assumed to be kind already --> contradiction 
                            flag = False
#                            print("Contradiction2")
                        else:
                            state = state & ~(1 << suspect - 1)                    
#                    print("after:", f"{state:05b} \n")

        if flag:
#            print("ans before:", ans)
            ans = max(ans, state.bit_count())
#            print("ans after:", ans)

    print(ans)

    
    

if __name__ == '__main__':
    main()
