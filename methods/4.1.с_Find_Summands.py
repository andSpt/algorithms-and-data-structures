def find_summands(n):
    summands = []
    current_summand = 1

    while n > current_summand * 2:
        summands.append(current_summand)
        n -= current_summand
        current_summand += 1

    summands.append(n)

    return summands

if __name__ == "__main__":
    n = int(input())
    summands = find_summands(n)
    print(len(summands))
    print(*summands)
