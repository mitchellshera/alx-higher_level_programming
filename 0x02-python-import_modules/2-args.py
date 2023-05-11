#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv) - 1

    if n == 0:
        print("No arguments.")
    else:
        argument_plural = "s" if n > 1 else ""
        print("{} argument{}{}:".format(n, argument_plural, ":"))

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
