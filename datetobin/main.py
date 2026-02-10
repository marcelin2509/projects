def datetobin(date: str) -> str:
    """Convert a date string in the format 'YYYY-MM-DD' to a binary string."""
    year, month, day = date.split('-')
    year_bin = format(int(year), '016b')  # 16 bits for the year
    month_bin = format(int(month), '08b')  # 8 bits for the month
    day_bin = format(int(day), '08b')      # 8 bits for the day
    return f"{year_bin}-{month_bin}-{day_bin}"

print("Enter a date in the format 'YYYY-MM-DD':")
date_input = str(input())
print("Binary representation:", datetobin(date_input))