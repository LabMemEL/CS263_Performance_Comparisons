import sys
import os
import psutil
import time


def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)

    return n


def main():
    start_wall = time.time()
    start_cpu = time.clock()
    start_core = psutil.cpu_times_percent(interval=None)

    n = fib(int(sys.argv[1]))
    print(n)

    end_wall = time.time()

    end_cpu = time.clock()
    end_core = psutil.cpu_times_percent(interval=None, percpu=True)

    # print('*'*50)
    process = psutil.Process(os.getpid())
    print('Total Wall Time: ', end_wall - start_wall, ' second')
    print('Total CPU Time: ', end_cpu - start_cpu, ' second')
    print('Total Memery Used: ', process.memory_info().rss, ' bytes')  # in bytes
    print('Total core util: ', end_core, ' percent')


if __name__ == '__main__':
    main()
