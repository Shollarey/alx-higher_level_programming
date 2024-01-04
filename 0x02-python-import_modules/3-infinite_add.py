#!/usr/bin/python3

if __name__ == "__main__":
    """Print result of the addition of all arguments"""
    import sys

    sum = 0
    count = len(sys.argv) - 1

    for i in range(count):
        sum += int(sys.argv[i+1])
    print(sum)
