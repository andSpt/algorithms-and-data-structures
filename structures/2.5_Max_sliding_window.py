from collections import deque


def max_sliding_window(nums, m):
    result = []
    window = deque()

    for i, num in enumerate(nums):
        while window and window[0] < i - m + 1:
            window.popleft()

        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= m - 1:
            result.append(nums[window[0]])

    return result


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())

    result = max_sliding_window(nums, m)
    print(*result)


if __name__ == "__main__":
    main()
