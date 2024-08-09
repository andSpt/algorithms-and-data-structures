def counting_sort(array, n):
    output = [0] * n
    count = [0] * 11

    for i in range(0, n):
        count[array[i]] += 1

    for i in range(1, 11):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    print(*output)


def main():
    n = int(input())
    array = list(map(int, input().split()))
    counting_sort(array, n)


if __name__ == "__main__":
    main()