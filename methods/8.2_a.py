def longest_subsequence(arr, n):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_subsequence(arr, n)
    print(result)


if __name__ == "__main__":
    main()