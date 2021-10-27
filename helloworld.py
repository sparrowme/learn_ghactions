import sys


def main():
    print("Hello World!" + str(sys.version_info) + str(sys.platform))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        # let's make this script fail for python 3.6
        raise Exception('Python version 3.6.x is unsupported!')


if __name__ == "__main__":
    main()

print("GitHub Actions")
