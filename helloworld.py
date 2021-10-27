import sys


def main():
    print("Hello World!")
    if sys.version_info == (3.6):
        # let's make this script fail for python 3.6
        x = 1/0


if __name__ == "__main__":
    main()

print("GitHub Actions")
