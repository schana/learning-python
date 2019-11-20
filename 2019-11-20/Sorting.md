# Sorting

## Bubble Sort

For each set of neighbors in a list, compare the items. Bubble up the lesser item. Continue doing this until there are no changes.

## List slicing

Colon notation `some_list[`*inclusive index*`:`*exclusive index*`]`

```python
my_list = list(range(10))
print(my_list[4:]) # [4, 5, 6, 7, 8, 9]
print(my_list[2:4]) # [2, 3]
```

## Merge Sort

Two step process:

1. Divide the list into singal elements
1. Progressively merge the divided elements in order

## Excercise

Implement the sort functions in the following program

```python
import random
import time

def bubble_sort(sortable):
    return []


def merge_sort(sortable):
    return []


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
```
