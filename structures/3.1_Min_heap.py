def sift_down(i, n, arr, swaps):
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child
    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))

        sift_down(min_index, n, arr, swaps)


def build_heap(arr, n):
    swaps = []

    for i in range(n // 2 -1, -1, -1):
        sift_down(i, n, arr, swaps)

    return swaps


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    swaps = build_heap(arr, n)

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
