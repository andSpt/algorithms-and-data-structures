from bisect import bisect_right
from random import choice


def quick_sort(array):
    if len(array) <= 1:
        return array

    random_index = choice(range(len(array)))
    less = []
    equal = []
    greater = []
    pivot = array[random_index]

    for num in array:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return quick_sort(less) + equal + quick_sort(greater)


# def binary_search_points(array, point):
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == point:
#             return mid + 1
#         elif array[mid] > point:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return left


def find_count_points_on_segments(points, points_start_segments, points_end_segments):
    sorted_starts_points_segments = quick_sort(points_start_segments)
    sorted_ends_points_segments = quick_sort(points_end_segments)
    result = []

    for point in points:
        # count_starts_points_left_target = binary_search_points(sorted_starts_points_segments, point)
        # count_ends_points_left_target = binary_search_points(sorted_ends_points_segments, point - 1)
        count_starts_points_left_target = bisect_right(sorted_starts_points_segments, point)
        count_ends_points_left_target = bisect_right(sorted_ends_points_segments, point - 1)
        total_count = count_starts_points_left_target - count_ends_points_left_target
        result.append(total_count)
    return result


def main():
    n, m = map(int, input().split())
    points_start_segments = []
    points_end_segments = []
    for _ in range(n):
        points_start_segment, point_end_segment = map(int, input().split())
        points_start_segments.append(points_start_segment)
        points_end_segments.append(point_end_segment)

    points = list(map(int, input().split()))

    print(*find_count_points_on_segments(points=points,
                                         points_start_segments=points_start_segments,
                                         points_end_segments=points_end_segments)
          )


if __name__ == "__main__":
    main()


