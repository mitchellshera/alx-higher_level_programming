#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    middle_index = int(size / 2)
    middle_element = list_of_integers[middle_index]
    
    left_neighbor = list_of_integers[middle_index - 1]
    right_neighbor = list_of_integers[middle_index + 1]

    if middle_element > left_neighbor and middle_element > right_neighbor:
        return middle_element
    elif middle_element < left_neighbor:
        return find_peak(list_of_integers[:middle_index])
    else:
        return find_peak(list_of_integers[middle_index + 1:])
