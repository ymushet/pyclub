from functools import reduce
from typing import List
import doctest


def multiplay_list(numbers: List[int]) -> int:
    """
    Returns summ of all elements of a list

    >>> multiplay_list([1, 5, 3])
    15
    >>> multiplay_list([])
    1
    """
    if not numbers:
        return 1

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
    >>> multiplication([1, 0, 2, 5, 8])
    [0, 80, 0, 0, 0]
    >>> multiplication([1, 0, 2, 0, 8])
    [0, 0, 0, 0, 0]
    """
    zero_count = numbers.count(0)
    if (zero_count >= 2):
        return [0] * len(numbers)

    if (zero_count == 1):
        n = multiplay_list([x for x in numbers if x != 0])
        return [
            0 if i != 0 else n
            for i in numbers
        ]

    value = multiplay_list(numbers)
    res = []
    for n in numbers:
        res.append(int(value / n))
    return res


if __name__ == "__main__":
    doctest.testmod()
