
import sys

def main():
    nmax = int(sys.stdin.readline())
    arr = set([int(i) for i in sys.stdin.readline().split()])
    nmin = 1
    for i in range(1, nmax+1):
        if i in arr: pass
        else:
            print(i)
    
if __name__ == '__main__':
    main()


