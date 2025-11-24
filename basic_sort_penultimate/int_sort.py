# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers using Bubble Sort, Quick Sort, and
Insertion Sort.
"""


def bubble(int_list):
    """
    Sort a list of comparable elements in ascending order using the
    Bubble Sort algorithm.

    Parameters
    ----------
    int_list : list
        The list of elements to be sorted.

    Returns
    -------
    list
        The sorted list.

    Source
    -------
    Adapted from https://www.w3schools.com/python/python_dsa_bubblesort.asp
    """

    length = len(int_list)  # Length of the list

    # Loop through all elements in the list
    for i in range(length):

        # Loop through remaining unsorted elements
        for j in range(0, length - i - 1):

            # Swap elements if they are in descending order
            if int_list[j] > int_list[j + 1]:
                temp = int_list[j]
                int_list[j] = int_list[j + 1]
                int_list[j + 1] = temp

    # Return the sorted list
    return int_list


def quick(int_list):
    """
    Sort a list of comparable elements in ascending order using the
    Quick Sort algorithm.

    Parameters
    ----------
    int_list : list
        The list of elements to be sorted.

    Returns
    -------
    list
        The sorted list.

    Source
    -------
    Adapted from https://www.geeksforgeeks.org/quick-sort/
    """

    length = len(int_list)
    stack = [(0, length - 1)]  # Use stack to store sublist boundaries
    while stack:  # Process each sublist until fully sorted
        low, high = stack.pop()

        if low < high:
            pivot = int_list[high]  # Choose pivot
            i = low - 1

            for j in range(low, high):  # Rearrange elements around the pivot
                if int_list[j] <= pivot:
                    i += 1
                    temp = int_list[i]
                    int_list[i] = int_list[j]
                    int_list[j] = temp

            # Place pivot in correct sorted position
            temp = int_list[i + 1]
            int_list[i + 1] = int_list[high]
            int_list[high] = temp

            pi = i + 1  # Pivot index

            # Add left and right partitions to the stack
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

    return int_list  # Return sorted list


def insertion(int_list):
    """
    Sort a list of comparable elements in ascending order using the
    Insertion Sort algorithm.

    Parameters
    ----------
    int_list : list
        The list of elements to be sorted.

    Returns
    -------
    list
        The sorted list.

    Source
    -------
    https://www.geeksforgeeks.org/python/python-program-for-insertion-sort/
    """
    length = len(int_list)
    for i in range(1, length):
        key = int_list[i]
        j = i - 1
        while j >= 0 and key < int_list[j]:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key
    return int_list
