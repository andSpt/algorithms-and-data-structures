from collections import deque


def process_packets(size_buffer, time_arrivals, time_durations):
    buffer = deque(maxlen=size)
    finish_process: int = 0
    result = []

    for arrival, duration in zip(time_arrivals, time_durations):
        current_time = arrival
        while buffer and current_time >= buffer[-1]:
            buffer.pop()

        if len(buffer) == size:
            result.append(-1)
        else:
            start_process = max(finish_process, arrival)
            result.append(start_process)
            finish_process = start_process + duration
            buffer.appendleft(finish_process)
    return result

size, num_packets = map(int, input().split())

arrivals: list = []

durations: list = []

for _ in range(num_packets):
    arr, dur = map(int, input().split())
    arrivals.append(arr)
    durations.append(dur)


results = process_packets(size_buffer=size, time_arrivals=arrivals, time_durations=durations)
for result in results:
    print(result)