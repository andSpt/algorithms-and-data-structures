import sys


def binary_search(array, length_array, value):
    left = 0
    right = length_array - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle + 1
        elif array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *a = next(reader)
    k, *b = next(reader)
    print(*[binary_search(array=a, length_array=n, value=element) for element in b])


if __name__ == "__main__":
    main()


