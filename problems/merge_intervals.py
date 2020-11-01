from typing import Callable, Iterable, List
import doctest


def is_overlap(a: int, b: int, c: int, d: int) -> bool:
    """"
    Determine if [a, b] and [c, d] overlaps

    >>> is_overlap(1, 2, 2, 3)
    True
    >>> is_overlap(1, 1, 1, 1)
    True
    >>> is_overlap(1, 2, 1, 2)
    True
    >>> is_overlap(1, 2, 3, 4)
    False
    >>> is_overlap(1, 3, 2, 6)
    True
    """
    if a <= d and b >= c:
        return True
    return False


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
    [-3, 0, 3, 3, 4, 5]
    """
    if not iterable:
        return []
    if key is None:
        key = lambda a: a

    numbers = [key(x) for x in iterable] # O (n)
    left = min(numbers)
    right = max(numbers)
    size = right - left + 1  # O(n)
    counters = [0] * size
    for n in numbers:  # O(n)
        counters[n - left] += 1

    result = []
    for i, c in enumerate(counters):  # O(k)
        value = [i + left] * c
        result.extend(value)
    return result  # O(n)


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    See https://leetcode.com/problems/merge-intervals/

    Extra: all numbers are integers (-2 ** 31, 2 ** 31)

    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5], [5, 6]])
    [[1, 6]]
    >>> merge([[1, 4], [5, 6]])
    [[1, 4], [5, 6]]
    >>> merge([[3, 5], [1, 4], [1, 3]])
    [[1, 5]]
    """

    if len(intervals) < 2:  # O(1)
        return intervals

    # TODO: best practice is not to modify the args
    intervals.sort(key=lambda x: x[0])  # O(n*log(n))

    res = [intervals[0]]  # O(1)

    for i in intervals[1:]:  # O(n)
        if is_overlap(*res[-1], *i):  # O(1)
            value = [min(*res[-1], *i), max(*res[-1], *i)]  # O(1)
            res.pop()  # O(1)
            res.append(value)  # O(1)
        else:
            res.append(i)  # O(1)
    return res  # O(n*log(n))


if __name__ == "__main__":
    # doctest.run_docstring_examples(is_overlap, globals())
    doctest.testmod()
    # print(count_sort([995, 996, 997, 998, 999, 1000]))
