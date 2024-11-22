import calendar


def display_calendar(year, month, day):
    try:
        return calendar.month(year, month, day)
    except month > 12:
        return f"month can't be greater than 12"


print(display_calendar(1995, 7, 17))
