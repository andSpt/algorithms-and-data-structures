# from abc import ABC, abstractmethod
#
#
# class MergeSort(ABC):
#     def __init__(self, arr):
#         self.arr = arr
#         self.inversions = 0
#
#     @abstractmethod
#     def sort(self):
#         pass
#
#     def _merge(self, left, right):
#         merged = []
#         left_index, right_index = 0, 0
#
#         while left_index < len(left) and right_index < len(right):
#             if left[left_index] <= right[right_index]:
#                 merged.append(left[left_index])
#                 left_index += 1
#             else:
#                 merged.append(right[right_index])
#                 right_index += 1
#                 self.inversions += len(left) - left_index
#
#         merged.extend(left[left_index:])
#         merged.extend(right[right_index:])
#
#         return merged
#
#
# class RecursiveMergeSort(MergeSort):
#     def sort(self):
#         if len(self.arr) <= 1:
#             return self.arr
#
#         mid = len(self.arr) // 2
#         left_half = self.arr[:mid]
#         right_half = self.arr[mid:]
#
#         left_merge_sort = RecursiveMergeSort(left_half)
#         right_merge_sort = RecursiveMergeSort(right_half)
#
#         left_sorted = left_merge_sort.sort()
#         right_sorted = right_merge_sort.sort()
#
#         return self._merge(left_sorted, right_sorted)
#
#
# class IterativeMergeSort(MergeSort):
#     def sort(self):
#         if len(self.arr) <= 1:
#             return self.arr
#
#         queue = []
#         for item in self.arr:
#             queue.append([item])
#
#         while len(queue) > 1:
#             first = queue.pop(0)
#             second = queue.pop(0)
#             merged = self._merge(first, second)
#             queue.append(merged)
#         return queue[0]
#
#
#
# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     recursive_merge_sort = RecursiveMergeSort(arr)
#     recursive_sorted_arr = recursive_merge_sort.sort()
#     inversions_recursive = recursive_merge_sort.inversions
#     print("Рекурсивная сортировка слиянием:")
#     print("Отсортированный массив:", recursive_sorted_arr)
#     print("Количество инверсий:", inversions_recursive)
#
#     iterative_merge_sort = IterativeMergeSort(arr)
#     iterative_sorted_arr = iterative_merge_sort.sort()
#     inversions_iterative = iterative_merge_sort.inversions
#     print("\nИтеративная сортировка слиянием:")
#     print("Отсортированный массив:", iterative_sorted_arr)
#     print("Количество инверсий:", inversions_iterative)
#
#
# if __name__ == "__main__":
#     main()


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count_inv_left = merge_sort(arr[:mid])
    right, count_inv_right = merge_sort(arr[mid:])
    merged, count_inv_merge = merge(left, right)

    count_inv_total = count_inv_left + count_inv_right + count_inv_merge
    return merged, count_inv_total


def merge(left, right):
    merged = []
    count_inv, i, j = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count_inv += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count_inv


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    merged, count_inv = merge_sort(arr)
    print(count_inv)


if __name__ == "__main__":
    main()
