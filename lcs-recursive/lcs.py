import sys
from pathlib import Path
import os
import psutil
import time


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
    start_wall = time.time()
    start_cpu = time.clock()
    start_core = psutil.cpu_times_percent(interval=None)

    lcs_str = lcs(sys.argv[1], sys.argv[2])
    print(lcs_str)

    end_wall = time.time()
    end_cpu = time.clock()
    end_core = psutil.cpu_times_percent(interval=None, percpu=True)

    process = psutil.Process(os.getpid())
    print('Total Wall Time: ', end_wall - start_wall, ' second')
    print('Total CPU Time: ', end_cpu - start_cpu, ' second')
    print('Total Memery Used: ', process.memory_info().rss, ' bytes')  # in bytes
    print('Total core util: ', end_core, ' percent')


if __name__ == '__main__':
    main()
