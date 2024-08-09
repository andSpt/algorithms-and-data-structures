import heapq
import sys


heap = []


def insert(num):
    heapq.heappush(heap, -num)


def extract_max():
    if heap:
        max_num = -heapq.heappop(heap)
        return max_num


def main():
    n = int(input())
    for _ in range(n):
        operation = input().split()
        if operation[0] == 'Insert':
            insert(int(operation[1]))
        else:
            if heap:
                print(extract_max())


if __name__ == '__main__':
    main()
