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


import pytest
import numpy as np
import psutil
from basic_sort_penultimate.int_sort import bubble


# =========================================================================
#  Fixtures
# =========================================================================

@pytest.fixture
def int_lists_dict():
    
    """
    Fixture providing a dictionary of test cases covering many classes of integer
    list scenarios.
    """

    return {
        "empty-list": [],
        "one-int": [4],
        "two-ints": [2, 1],
        "sorted-list": [-200, -49, -1, 0, 5, 38, 84, 190],
        "reverse-list": [100, 10, 3, 2, 1, 0, -10, -28],
        "uniform-list": [1, 1, 1, 1, 1, 1],
        "positive-ints": [105, 24, 5, 209, 2, 1039, 92, 90],
        "negative-ints": [-24, -13, -90, -2, -17, -394, -1, -9],
        "repeating-positive-int": [5, 5, 61, 5, 43, 61, 61, 5],
        "repeating-negative-int": [-7, 3, -7, -7, 5, 0, -3],
        "random-ints": np.random.randint(low=-10, high=200, size=5)
        
    }


# =========================================================================
#  Helper Functions
# =========================================================================

def is_sorted(int_list):
    """
    Validates if a list of integers is sorted in ascending order.

    Parameters
    ----------
    int_list : list
        The list of integers to check for sorted order.

    Returns
    -------
    bool
        True if the list is sorted in ascending order, False otherwise.
    """
    lst = list(int_list) # Convert NumPy array to list
    return lst == sorted(lst)


# =========================================================================
#  Functional Tests
# =========================================================================  

def test_bubble(int_lists_dict):
    """
    Test the bubble sort implementation across all test cases.

    Parameters
    ----------
    int_lists_dict : dict
        A dictionary of test case names mapped to lists of integers.

    Asserts
    -------
    The output of bubble() must be sorted for each input case.
    """
    
    for test_name, data in int_lists_dict.items():
        sorted_list = bubble(data.copy())
        assert is_sorted(sorted_list), f"Bubble Sort failed on case: {test_name}"

def test_quick(int_lists_dict):
    assert True

def test_insertion(int_lists_dict):
    assert True


# =========================================================================
#  Performance Tests
# =========================================================================  

def test_bubble_cpu(int_lists_dict):
    """
    Measure CPU usage of Bubble Sort across all provided test cases.

    Parameters
    ----------
    int_lists_dict : dict
        Dictionary mapping test case names to lists of integers.

    Source
    -------
    References https://psutil.readthedocs.io/en/latest/
    """

    process = psutil.Process()
    process.cpu_percent(interval=None)  # Baseline measurement

    # Run Bubble Sort on all test cases
    for case_data in int_lists_dict.values():
        bubble(case_data.copy())

    cpu_used = process.cpu_percent(interval=None)
    print(f"Total CPU usage for all Bubble Sort test cases: {cpu_used:.2f}%")