from datetime import datetime, timedelta

# Replace with your birthday (day, month)
birthday_day = 15
birthday_month = 10

today = datetime.today()
birthday = datetime(today.year, birthday_month, birthday_day)

# If birthday already passed this year, take next year
if birthday < today:
    birthday = birthday.replace(year=today.year + 1)

days_left = (birthday - today).days
print(f"Days until your birthday: {days_left}")