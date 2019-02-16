
import sys
import array
import os
import psutil
import time

# reference: http://www.syntagmatic.net/matrix-multiplication-in-python/


def matmul(a, b):  # FIXME: no error checking
    ra, rb, rb0 = list(range(len(a))), list(
        range(len(b))), list(range(len(b[0])))
    c = [array.array('d', [b[j][i] for j in rb]) for i in rb0]
    d = [array.array('d', [0 for j in rb0]) for i in ra]  # transpose
    for i in ra:
        for j in rb0:
            s, ai, cj = 0, a[i], c[j]
            for k in rb:
                s += ai[k] * cj[k]
            d[i][j] = s
    return d


def main():
    n = 100
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    n = int(float(n)/2) * 2
    tmp = 1. / n / n
    a = [[tmp * (i - j) * (i + j) for j in range(n)] for i in range(n)]
    b = [[tmp * (i - j) * (i + j) for j in range(n)] for i in range(n)]
    d = matmul(a, b)
    print(d[int(n/2)][int(n/2)])


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()

    print('*'*50)
    process = psutil.Process(os.getpid())
    print('Total Execution Time: ', end - start, ' second')
    print('Total Memery Used: ', process.memory_info().rss, ' bytes')  # in bytes
