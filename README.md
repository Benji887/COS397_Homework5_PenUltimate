## Code Formatting Rules

-Pre-commit hooks: will auto run before each commit, detects AWS credentials to make sure there are none and limits file size.

-Black: auto formatting for code, has line limit of 88 char, double quotes are preferred, indents of 4 spaces.

-Flake8: Python style checker: need to fix all warnings/errors before committing, avoid including vars/imports in code that aren't used.

## Git Hooks Setup

Once repo is cloned in your environment, run "pip install pre-commit" to install the python package, then run "pre-commit install" to read the pre commit file and set up the Git hooks. After that, the hooks should be active. You can manually trigger the checks on all files by running "pre-commit run --all-files".
