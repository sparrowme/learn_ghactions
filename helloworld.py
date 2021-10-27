import sys


def main():
    print(f"Hello World!" + str(sys.version_info) + str(sys.platform))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        # let's make this script fail for python 3.6
        x = 1/0
    if sys.platform == 'darwin':
        x = 1/0


if __name__ == "__main__":
    main()

print("GitHub Actions")
