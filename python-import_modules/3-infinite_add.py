#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg = len(argv)
    if (arg == 0):
        print("0")
    else:
        c = 0
        for a in range(arg):
            c += int(argv[a])
        print("{}".format(c))
