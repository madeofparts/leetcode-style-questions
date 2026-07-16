
import sys

def main():
    nmax = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    xor = 0

    for i in range(1, nmax):
        xor ^= i
        xor ^= arr[i-1]
    xor ^= nmax
    print(xor)

if __name__ == '__main__':
    main()


