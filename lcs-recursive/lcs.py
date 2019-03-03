import sys
from pathlib import Path


def lcs(xstr, ystr):
    if (xstr == "" or ystr == ""):
        return ""

    x = xstr[0]
    xs = xstr[1:]
    y = ystr[0]
    ys = ystr[1:]

    if x == y:
        return(x + lcs(xs, ys))

    lcs1 = lcs(xstr, ys)
    lcs2 = lcs(xs, ystr)

    if len(lcs1) > len(lcs2):
        return lcs1
    else:
        return lcs2


def main():
    lcs_str = lcs(sys.argv[1], sys.argv[2])
    print(lcs_str)


if __name__ == '__main__':
    main()
