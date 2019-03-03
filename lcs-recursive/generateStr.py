import string
import random
import sys


def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for m in range(length))


def main():
    n = int(sys.argv[1])
    random_str1 = random_string(n)
    random_str2 = random_string(n)
    print(random_str1 + ' ' + random_str2)


if __name__ == '__main__':
    main()
