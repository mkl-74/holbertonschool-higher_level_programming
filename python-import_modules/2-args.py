#!/usr/bin/python3
import sys

def main():
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print(f"{arg_count} arguments.")
    elif arg_count == 1:
        print(f"{arg_count} argument:")
    else:
        print(f"{arg_count} arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    main()
