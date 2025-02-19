def add_days(date, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    split_date = date.split("-")
    days = int(split_date[2])
    month = int(split_date[1])
    year = int(split_date[0])
    while n > 0:
        if is_leapyear(year):
            days_in_month[2] = 29
        else:
            days_in_month[2] = 28
        if n + days > days_in_month[month]:
            rems = days_in_month[month] - days
            n -= rems + 1
            days = 1
            month += 1
        else:
            days += n
            n = 0
        if month > 12:
            month = 1
            year += 1
    return f"{year}-{month:02d}-{days:02d}"


def is_leapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    pass