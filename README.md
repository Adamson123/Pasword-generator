# Password Generator (Python)

A simple CLI tool that creates a random password with a mix of lowercase, uppercase, digits, and special characters.  
This is my first Python project.

-   Main script: [passwordGenerator.py](c:\Users\Admin\Desktop\Password-generator\passwordGenerator.py)
-   Core functions:
    -   [`validateLength`](c:\Users\Admin\Desktop\Password-generator\passwordGenerator.py)
    -   [`getAmountForEachCharacters`](c:\Users\Admin\Desktop\Password-generator\passwordGenerator.py)
    -   [`pickRandomCharacter`](c:\Users\Admin\Desktop\Password-generator\passwordGenerator.py)
    -   [`generatePassword`](c:\Users\Admin\Desktop\Password-generator\passwordGenerator.py)

## Requirements

-   Python 3.7+
-   Windows (examples below use PowerShell/CMD)

## Run from the command line

From the project folder:

1. Open a terminal in the project directory:
    - PowerShell: `cd "C:\Users\Admin\Desktop\Password-generator"`
    - CMD: `cd C:\Users\Admin\Desktop\Password-generator`
2. Show help:
    - `py .\passwordGenerator.py -h`
3. Generate a password:
    - `py .\passwordGenerator.py 12`
    - or: `python .\passwordGenerator.py 12`
    - also works: `py passwordGenerator.py 30`

Quick run example (rendered as Python per request):

```py
py .\passwordGenerator.py 30
```

Examples:

-   Invalid (too short): `py .\passwordGenerator.py 5` → exits with: `Length should be >= 6`
-   Missing argument: `py .\passwordGenerator.py` → argparse shows usage and exits.

Tip: Check Python is available:

-   `py --version` or `python --version`

## Use as a library

```py
from passwordGenerator import generatePassword
print(generatePassword(12))
```

## How it works

-   Target mix (default): ~40% lowercase, ~25% uppercase, ~20% digits, ~15% special.
-   Exact counts are computed in [`getAmountForEachCharacters`](c:\Users\Admin\Desktop\Learn-python\passwordGenerator.py) using rounding; any remainder is added to lowercase.
-   Characters are picked randomly per category in [`generatePassword`](c:\Users\Admin\Desktop\Learn-python\passwordGenerator.py).

## Exit behavior

-   If the length is invalid or < 6, [`validateLength`](c:\Users\Admin\Desktop\Learn-python\passwordGenerator.py) calls `sys.exit(...)`, causing the program to exit with an error.
