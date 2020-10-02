from typing import List
import doctest


def is_overlap(a : int, b : int, c : int, d : int) -> bool:
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
    """
    if b == c:
        return True
    elif a >= c and c <= b:
        return True
    elif a >= d and d <= b:
        return True

    return False


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    See https://leetcode.com/problems/merge-intervals/

    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    """
    intervals.sort(key=lambda a: a[0])
    # TODO: Merge lists now


if __name__ == "__main__":
    doctest.run_docstring_examples(is_overlap, globals())
