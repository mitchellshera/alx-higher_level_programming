#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_arguments = len(argv) - 1
    argument_plural = "argument" if num_arguments == 1 else "arguments"
    punctuation = "." if num_arguments == 0 else ":"

    print("{} {}{}{}".format(num_arguments, argument_plural, punctuation,
                             "\n" if num_arguments > 0 else ""), end="")

    for i, s in enumerate(argv[1:], start=1):
        print("{:d}: {:s}".format(i, s))
