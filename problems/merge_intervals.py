from typing import Callable, Iterable, List
import doctest


def count_sort(iterable : Iterable, key : Callable = None):
    """
    >>> count_sort([])
    []
    >>> count_sort([0, 1, 2, 3, 4])
    [0, 1, 2, 3, 4]
    >>> count_sort([4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4]
    >>> count_sort([4, 3, 3, 3, 0])
    [0, 3, 3, 3, 4]
    >>> count_sort([4, 3, -3, 3, 0])
    [-3, 0, 3, 3, 4]
    >>> count_sort('defcba', key=ord)
    ['a', 'b', 'c', 'd', 'e', 'f']
    """
    if not iterable:
        return []

    if key is None:
        key = lambda a: a

    numbers = [key(x) for x in iterable]  # O(n)
    assert all(type(n) is int for n in numbers)

    # buckets = collections.defaultdict(list)
    # for i, n in zip(iterable, numbers):
    #     buckets[n].append(i)
    # sorted_keys = sorted(bucket.keys())  # O(k*log(k))

    left = min(numbers)
    right = max(numbers)
    size = right - left + 1  # O(n)
    counters = [[] for _ in range(size)]

    for n, i in zip(numbers, iterable):  # O(n)
        counters[n - left].append(i)

    [
        [(1, 2), (1, 3)],  # bucket0
        [],  # bucket 1
        [],
    ]
    result = []  # TODO: itertools.chain
    for c in counters:
        result.extend(c)
    return result


if __name__ == "__main__":
    # doctest.run_docstring_examples(is_overlap, globals())
    doctest.testmod()
    # print(count_sort([995, 996, 997, 998, 999, 1000]))
    # count_sort([4, 3, -3, 3, 0])
