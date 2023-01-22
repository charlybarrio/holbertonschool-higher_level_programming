#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg = len(argv)
    if (arg == 0):
        print("{} arguments.".format(arg))
    else:
        print("{} argument:".format(arg))
        for a in range(arg):
            print("{}: {}".format(a + 1, argv[a]))
