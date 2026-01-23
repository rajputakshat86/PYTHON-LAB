day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month in [1,3,5,7,8,10,12]:
    max_day = 31
elif month in [4,6,9,11]:
    max_day = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_day = 29
    else:
        max_day = 28

day += 1
if day > max_day:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print(f"Next Date: day={day} month={month} year={year}")
