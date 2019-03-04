import sys
import re
from timeit import default_timer as timer
import os
import psutil
import time


if len(sys.argv) != 2:
    print('Usage: python benchmark.py <filename>')
    sys.exit(1)


def measure(data, pattern):
    start_wall = time.time()
    start_cpu = time.clock()
    start_core = psutil.cpu_times_percent(interval=None)

    regex = re.compile(pattern)
    matches = re.findall(regex, data)

    end_wall = time.time()

    end_cpu = time.clock()
    end_core = psutil.cpu_times_percent(interval=None, percpu=True)

    # print('*'*50)
    process = psutil.Process(os.getpid())
    print('Total Wall Time: ', end_wall - start_wall, ' second')
    print('Total CPU Time: ', end_cpu - start_cpu, ' second')
    print('Total Memery Used: ', process.memory_info().rss, ' bytes')  # in bytes
    print('Total core util: ', end_core, ' percent')


with open(sys.argv[1]) as file:
    data = file.read()

    # Email
    measure(data, '[\w\.+-]+@[\w\.-]+\.[\w\.-]+')

    # URI
    measure(data, '[\w]+://[^/\s?#]+[^\s?#]+(?:\?[^\s#]*)?(?:#[^\s]*)?')

    # IP
    measure(
        data, '(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])')
