from typing import List
import doctest


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    See https://leetcode.com/problems/merge-intervals/

    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    """
    intervals.sort(key=lambda a: a[0])


if __name__ == "__main__":
    """
    merge([[5, 6], [3, 4], [1, 2]])
    >>> [[1, 7], [3, 4], [5, 6]]
    """
    doctest.testmod()