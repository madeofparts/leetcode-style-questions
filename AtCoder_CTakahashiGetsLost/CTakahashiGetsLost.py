# Problem: C - Takahashi Gets Lost
# Contest: Toyota Programming Contest 2024#2（AtCoder Beginner Contest 341）
# Judge: AtCoder
# URL: https://atcoder.jp/contests/abc341/tasks/abc341_c
# Memory Limit: 1024
# Time Limit: 3000
# Start: Thu 16 Jul 2026 08:49:29 PM

def main():
    h,w,n = map(int, input().split())
    t = input()
    c = [input() for _ in range(h)]

    count = 0

    # simulate for each inner (non-outer/sea) cell
    for y in range(1,h-1):
        for x in range(1,w-1):
            x_0 = x
            y_0 = y
            # check that the starting cell is a valid cell
            if c[y_0][x_0] == "#": continue

            # simulate each instruction
            for m in t:
                match m:
                    case "L":
                        x_0 -= 1 
                    case "R":
                        x_0 += 1 
                    case "U": 
                        y_0 -= 1 
                    case "D":
                        y_0 += 1 

                if c[y_0][x_0] == "#":
                    break
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
