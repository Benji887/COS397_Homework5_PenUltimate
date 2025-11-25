## Code Formatting Rules

-Pre-commit hooks: will auto run before each commit, detects AWS credentials to make sure there are none and limits file size.

-Black: auto formatting for code, has line limit of 88 char, double quotes are preferred, indents of 4 spaces.

-Flake8: Python style checker: need to fix all warnings/errors before committing, avoid including vars/imports in code that aren't used.

## Git Hooks Setup

Once repo is cloned in your environment, run "pip install pre-commit" to install the python package, then run "pre-commit install" to read the pre commit file and set up the Git hooks. After that, the hooks should be active. You can manually trigger the checks on all files by running "pre-commit run --all-files".

If after entering "pip install pre-commit" you are not able to run the command "pre-commit install". Enter "python -m pre_commit run --all-files".

## Steps to Run Sorting Algorithm Tests

-Ensure you are entering commands from the root of the project directory "COS397_Homework5_PenUltimate".

-Download all libraries and packages located in the "requirements.txt" file. Using "pip install ______".

-Enter "python -m pytest -s" command.

## File Description

-main.yml: Contains the GitHub actions workflow that runs the sorting algorithms on Python versions 3.9, and 3.10. It runs these algorithms on Linux, macOS, and Windows operating systems. Runs tests for each of the three sorting algorithms.

-int-sort.py: Contains sorting algorithms that sort a list of integers. The sorting algorithms are bubble, quick, and insertion sort.

-test_basic_sort.py: This file includes the tests that are ran on each of the three sorting algorithms. 

-.flake8: Limits the maximum line length using linting.

-.gitignore: Includes pycache and macOS metadata files.

-.pre-commit-config.yaml: Limits maximal file size, detects AWS key, checks formatting, and lints using flake8.

-INSTRUCTIONS.md: Contains the instructions for the homework assignment provided by Professor Yoo.

-LICENSE: Contains the GitHub license that was chosen when this repository was created.

-README.md: Contains information on how to run the tests for the sorting algorithms, libraries needed for running the tests, file descriptions of all files within the repository, directions to run tests, and output of tests.

-pyproject.toml: Contains various configuration file standards used in this repository such as build system, and project description.

-requirements.dev.txt: Contains various libraries and packages needed for running the algorithms, and tests within the repository.

-requirements.txt: Contains various libraries needed for running the algorithms, and tests within the repository.

## Test Output

Bubble Sort CPU time: 0.000028 seconds
Quick Sort runtime: 0.000049 seconds
Insertion Sort memory allocated: 0.6406 KB
