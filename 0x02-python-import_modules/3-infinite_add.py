#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    result = 0

    for args in sys.argv:
        if args != sys.argv[0]:
            result += int(args)
    print("{}".format(result))
