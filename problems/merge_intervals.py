from typing import List
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


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    See https://leetcode.com/problems/merge-intervals/

    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5], [5, 6]])
    [[1, 6]]
    >>> merge([[1,4],[5,6]])
    [[1, 4], [5, 6]]
    """
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda a: a[0])
    res = []
    for i in range(1, len(intervals)):
        if is_overlap(*intervals[i - 1], *intervals[i]):
            res.append([min(*intervals[i-1], *intervals[i]), max(*intervals[i-1], *intervals[i])])
        else:
            res.append(intervals[i])

    return res


if __name__ == "__main__":
    #doctest.run_docstring_examples(is_overlap, globals())
    doctest.testmod()
