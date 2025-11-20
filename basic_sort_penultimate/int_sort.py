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
    Adapted from https://https://www.w3schools.com/python/python_dsa_bubblesort.asp
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
    qsort docstring
    """
    print("quick sort")


def insertion(int_list):
    """
    insertion docstring
    adapted from https://www.geeksforgeeks.org/python/python-program-for-insertion-sort/
    """
    length = len(int_list)
    for i in range(1, length):
        key = int_list[i]
        j = i - 1
        while j >= 0 and key < int_list[j]:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key
    print("insertion sort")
    return int_list
