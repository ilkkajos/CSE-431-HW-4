from typing import TypeVar, List, Callable
import unittest
from random import seed, sample, randint, shuffle
import copy

T = TypeVar("T")            # represents generic type


def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]

def merge(S1: List[T], S2: List[T], S: List[T], counter: int = 0,
          comparator: Callable[[T, T], bool] = lambda x, y: x <= y):
    n = len(S)
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and comparator(S1[i], S2[j])):
            S[i + j] = S1[i]
            i = i + 1
        else:
            S[i + j] = S2[j]
            counter = counter + len(S1[i:n - 1])
            j = j + 1
    return counter

def merge_sort(data: List[T], threshold: int = 0,
               comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> int:
    """
    Given a list of values, perform a merge sort to sort the list and calculate the inversion count. When a threshold is provided, use a merge sort algorithm until the partitioned lists are smaller than or equal to the threshold - then use insertion sort. Be sure to use the comparator.
param data: List of items to be sorted.
param threshold: int representing the size of the data at which insertion sort should be used. Defaults to 0.
param comparator: A function, which takes an argument two objects of like type to those in the list data and returns `True` if the first argument is less than or equal to the second according to some ordering, else `False`.
return: int representing inversion count, else 0 if threshold > 0.
Time Complexity: O(nlog(n))
Space Complexity: O(n)
    """

    n = len(data)
    if n < 2:
        return 0
    if n <= threshold:
        insertion_sort(data, comparator)
        return 0
    mid = n // 2
    S1 = data[0:mid]
    S2 = data[mid:n]
    a = merge_sort(S1, threshold, comparator)
    b = merge_sort(S2, threshold, comparator)
    count = merge(S1, S2, data, 0, comparator)
    return count+b+a

def insertion_sort(data: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Given a list of values and comparator, perform an insertion sort on the list using the comparator.
param data: List of items to be sorted
param comparator: A function, which takes an argument two objects of the same type as those in the list data and returns `True` if the first argument is less than or equal to the second according to some ordering, else `False`.
return: None
Time Complexity: O(n^2)
Space Complexity: O(1]
    """

    n = len(data)
    for i in range(1, n):
        j = i
        while (j > 0) and (comparator(data[j], data[j - 1])):
            exchange(data, j, j - 1)
            j -= 1

def hybrid_sort(data: List[T], threshold: int,
                comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Wrapper function to call merge_sort() as a Hybrid Sorting Algorithm. Should call merge_sort() with provided threshold, and comparator function.
    param data: List of items to be sorted.
    param threshold: int representing the size of the data at which insertion sort should be used.
    param comparator: A function, which takes an argument two objects of like type to those in the list data and returns `True` if the first argument is less than or equal to the second according to some ordering, else `False`.
    return: None
    Time Complexity: O(nlog(n))
    Space Complexity: O(n)
    """
    merge_sort(data, threshold, comparator)

seed(331)

class HW4Tests(unittest.TestCase):

    def test_hybrid_sort_speed(self):
        # The point of this sort is to be fast, right?
        # This (probably) won't pass if you're not careful with time complexity
        data = list(range(100000))
        expected = data[:]
        shuffle(data)
        hybrid_sort(data, threshold=12)
        self.assertEqual(expected, data)

if __name__ == '__main__':

    unittest.main()

