import calendar
from datetime import date


def days_in_month(year: int, month: int) -> int:
  
    return calendar.monthrange(year, month)[1]


def calculate_age(dob: date, today: date | None = None) -> tuple[int, int, int]:
    
    today = today or date.today()
    if dob > today:
        raise ValueError("Date of birth cannot be in the future.")

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    
    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += days_in_month(prev_year, prev_month)

    
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def parse_dob(text: str) -> date:
    
    cleaned = text.strip().replace("/", "-").replace(".", "-")
    parts = cleaned.split("-")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise ValueError("Invalid format. Please use DD-MM-YYYY (e.g. 29-02-2000).")

    day, month, year = map(int, parts)

    if year < 1 or year > date.today().year:
        raise ValueError(f"Year must be between 1 and {date.today().year}.")
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")
    if not 1 <= day <= days_in_month(year, month):
        raise ValueError(
            f"{calendar.month_name[month]} {year} has only "
            f"{days_in_month(year, month)} days."
        )

    dob = date(year, month, day)
    if dob > date.today():
        raise ValueError("Date of birth cannot be in the future.")
    return dob


def plural(n: int, word: str) -> str:
    return f"{n} {word}{'' if n == 1 else 's'}"


def main() -> None:
    print("=" * 40)
    print("          AGE CALCULATOR")
    print("=" * 40)
    print("Enter date of birth as DD-MM-YYYY. Type 'q' to quit.\n")

    while True:
        text = input("Date of birth: ").strip()
        if text.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        try:
            dob = parse_dob(text)
            years, months, days = calculate_age(dob)
        except ValueError as err:
            print(f"  Error: {err}\n")
            continue

        total_days = (date.today() - dob).days
        print(f"\n  Born on : {dob.strftime('%d %B %Y')} ({dob.strftime('%A')})")
        print(
            f"  Age     : {plural(years, 'year')}, "
            f"{plural(months, 'month')}, {plural(days, 'day')}"
        )
        print(f"  Total   : {total_days:,} days lived\n")


if __name__ == "__main__":
    main()