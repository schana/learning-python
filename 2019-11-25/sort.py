import random
import time

def bubble_sort(sortable):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sortable) - 1):
            if sortable[i + 1] < sortable[i]:
                sortable[i], sortable[i + 1] = sortable[i + 1], sortable[i]
                swapped = True
    return sortable


def merge_sort(sortable):
    return divide(sortable)


def divide(sortable):
    if len(sortable) <= 1:
        return sortable
    return merge(divide(sortable[:len(sortable) // 2]), divide(sortable[len(sortable) // 2:]))


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    return merged + left[left_index:] + right[right_index:]


def do_sort(method, sortable):
    start_time = time.time()
    sorted_list = method(sortable[:])
    elapsed_time = time.time() - start_time
    correct = sorted_list == sorted(sortable)
    print('{} executed in {} seconds {}'.format(method.__name__, elapsed_time, 'correctly' if correct else 'incorrectly'))


def main():
    original = [random.random() for i in range(2000)]
    do_sort(bubble_sort, original)
    do_sort(merge_sort, original)


if __name__ == '__main__':
    main()
