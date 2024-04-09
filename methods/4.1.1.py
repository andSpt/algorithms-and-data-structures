def get_optimal_points(list_segments):
    points = []
    sorted_list_segments: list = sorted(list_segments, key=lambda x: x[1])
    current_point = sorted_list_segments[0][1]
    points.append(current_point)

    for segment in sorted_list_segments:
        start, end = segment
        if current_point < start or current_point > end:
            current_point = end
            points.append(current_point)

    return points


if __name__ == "__main__":
    n = int(input())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    result = get_optimal_points(segments)
    print(len(result), *result, sep='\n')