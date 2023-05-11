#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    m = len(argv)
    print("{:d} {:s}{:s}".format(m - 1, "argument" if m <= 2 else "arguments",
                                 "." if m == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
