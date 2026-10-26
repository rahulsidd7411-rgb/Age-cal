# Age Calculator

A simple command-line application in Python that calculates your exact age in **years, months and days** from your date of birth.

## Features

- Accurate age calculation with correct handling of **leap years** and **variable month lengths**
- Input validation: rejects invalid formats, non-existent dates (e.g. 31-04-2000, 29-02-2001) and **future dates**
- Interactive CLI: calculate as many ages as you like without restarting
- Also shows the weekday you were born on and total days lived
- No external libraries required (uses only Python's standard library)

## Requirements

- Python 3.10 or newer

## Usage

```bash
python age_calculator.py
```

Enter your date of birth as `DD-MM-YYYY` (the separators `/` and `.` also work). Type `q` to quit.

## Example

```
========================================
          AGE CALCULATOR
========================================
Enter date of birth as DD-MM-YYYY. Type 'q' to quit.

Date of birth: 29-02-2000

  Born on : 29 February 2000 (Tuesday)
  Age     : 26 years, 7 months, 27 days
  Total   : 9,736 days lived

Date of birth: 31-04-2000
  Error: April 2000 has only 30 days.
```

## How it works

- `calculate_age()` subtracts the dates and borrows days from the previous month and months from the year when needed, using `calendar.monthrange` for the real month length.
- `parse_dob()` validates the format, year, month, day and rejects future dates.

## Author

Rahul
