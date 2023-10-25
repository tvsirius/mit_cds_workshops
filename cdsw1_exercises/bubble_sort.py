#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def bubble_sort(task_list: list) -> list:
    """ Sorts a list in place and returns a sorted list

    :param task_list: list of elements, that allow comparasions (int, float, char)
    :return: sorted list

    >>> bubble_sort([])
    []

    >>> bubble_sort([2])
    [2]

    >>> bubble_sort([1,8,-2,3])
    [-2, 1, 3, 8]

    >>> bubble_sort(['r','a','z','f'])
    ['a', 'f', 'r', 'z']
    """

    # assert correct params
    assert isinstance(task_list, list), "task_list must be list"

    # Getting list size for comfort use
    list_size = len(task_list)

    # each iteration will move the biggest element to the end of the list,
    # so will need list_size number of iteration for sorting all elements
    for i in range(list_size):

        # the (i) last elements are already sorted
        for j in range(0, list_size - i - 1):

            # do the bubble! (if task_list[0] is the biggest element of this iteration
            # [0..list_size - i - 1], it will reach the end with it
            if task_list[j] > task_list[j + 1]:
                task_list[j], task_list[j + 1] = task_list[j + 1], task_list[j]

    return task_list
