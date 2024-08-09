def longest_subsequence(arr, n):
    dp = [1] * n
    subsequence_indices = []

    for i in range(1, n):
        for j in range(i):
            if arr[i] <= arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    index = dp.index(max_length)
    subsequence_indices.append(index + 1)
    current_len = max_length - 1

    for i in range(index - 1, -1, -1):
        if dp[i] == current_len and arr[i] >= arr[index]:
            subsequence_indices.append(i + 1)
            index = i
            current_len -= 1

    return max_length, subsequence_indices[::-1]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    length_sequence, indices = longest_subsequence(arr, n)
    print(length_sequence)
    print(*indices)


if __name__ == "__main__":
    main()