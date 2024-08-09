import heapq

def parallel_processing(n, tasks):
    processors = [(0, i) for i in range(n)]
    result = []

    for i, task_time in enumerate(tasks):
        time, processor_index = heapq.heappop(processors)
        result.append((processor_index, time))
        heapq.heappush(processors, (time + task_time, processor_index))

    return result


def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    output = parallel_processing(n, tasks)
    for proc, time in output:
        print(proc, time)


if __name__ == "__main__":
    main()