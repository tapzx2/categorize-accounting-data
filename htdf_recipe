# Read Me

problem: I really don't want to do our accounting each year. It involves:

- labeling each expense
- summing values of each expense
- submitting to accountant

## Basic Sketch

```text
Display csv file, line by line
Get user input
Append user input to outputfile
```

Current goal:

mvp. Don't offer command options.

End goal:

```text
"""
    NAME
        run.py -- utility to make small business accounting easier
    
    SYNOPSIS
        run.py --separate="FILE_PATH" | --categorize="FILE_PATH" [--common="FILE_PATH"] [--categories="FILE_PATH"]

    DESCRIPTION
        The following options are available:

        --separate    Separate transactions file into income.csv and expenses.csv. Will error if there are transactions of zero.

        --categorize  Adds column to file and prompts user for categorization of each transaction. Once in this mode adjustments to common values and acceptable categorize can be made.

        --common      Specifies custom file for common values. File must be in .json format.

        --categories  Specifies custom file for category values. File must be in .json format.
"""
```

Once in categorize mode commands to add:

- save changes
- quit
- start again from last point
- add a common value
- add a category
