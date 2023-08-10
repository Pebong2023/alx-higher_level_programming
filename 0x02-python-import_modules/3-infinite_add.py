#!/usr/bin/python3

import sys

def main():
    """Print the sum of all arguments."""
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("{}".format(total))

if __name__ == "__main__":
    main()
