import calendar

month, day, year = map(int, (input().split()))

c = calendar.day_name[calendar.weekday(year=year, month=month, day=day)].upper()
print(c)
