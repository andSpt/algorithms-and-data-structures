def get_optimal_points(list_segments):
    sorted_list_segments: list = sorted(list_segments, key=lambda x: (x[1], x[0]))
    current_point = sorted_list_segments[0][1]
    optimal_points = [current_point]

    for start, end in sorted_list_segments[1:]:
        if start > current_point:
            current_point = end
            optimal_points.append(current_point)

    return optimal_points


if __name__ == "__main__":
    n = int(input())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    result = get_optimal_points(segments)
    print(len(result), *result, sep='\n')