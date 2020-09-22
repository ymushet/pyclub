from functools import reduce
from typing import List
import doctest


def cut_list(numbers: List[int], index: int) -> List[int]:
    pass


def multiplay_list(numbers: List[int]) -> int:
    """
    Returns summ of all elements of a list

    >>> multiplay_list([1, 5, 3])
    15
    >>> multiplay_list([])
    0
    """
    if not numbers:
        return 0

    return reduce((lambda x, y: x * y), numbers)


def multiplication(numbers: List[int]) -> List[int]:
    """
    Given a sequence of integers. Build a new sequence of the same length. Each element of a new
    sequence should be calculated as a multiplication of elements of the original sequence except
    the element with the same index.  Think about possible corner cases.

    >>> multiplication([1, 5, 3])
    [15, 3, 5]
    >>> multiplication([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    """
    res = []
    for n in numbers:
        index = numbers.index(n)
        res.append(multiplay_list(cut_list(numbers, index)))

    return res


if __name__ == "__main__":
    #doctest.testmod()
    doctest.run_docstring_examples(multiplay_list, globals())
