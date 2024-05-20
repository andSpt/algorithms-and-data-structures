def knapsack(knapsack_capacity, item_weights, n):
    d = [[0 for _ in range(knapsack_capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, knapsack_capacity + 1):
            if item_weights[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = max(d[i - 1][w], d[i - 1][w - item_weights[i - 1]] + item_weights[i - 1])

    return d[n][knapsack_capacity]


def main():
    knapsack_capacity, n = map(int, input().split())
    item_weights = list(map(int, input().split()))

    result = knapsack(knapsack_capacity, item_weights, n)
    print(result)


if __name__ == "__main__":
    main()
