def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


def fib_mod(n, m):
    period = get_pisano_period(m)
    remainder = n % period
    fib = [0, 1]
    for i in range(2, remainder + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % m)
    return fib[remainder]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
