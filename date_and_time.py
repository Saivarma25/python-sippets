"""
Task on Date & Time
"""

"""
Get current date and time — Print current date, time, and weekday name.
"""
from datetime import datetime, timedelta
import time

print(datetime.today())


"""
Format a date — Convert current date to format YYYY-MM-DD or DD-MM-YYYY.
"""
date = datetime.today()

date_ymd = date.strftime('%Y-%m-%d')
date_dmy = date.strftime('%d-%m-%Y')
print(date_ymd)
print(date_dmy)

"""
"""

age_str = input("Enter your date of birth (dd-mm-yyyy): ")

try:
    dob: datetime = datetime.strptime(age_str, '%d-%m-%Y')
    
    age = date.year - dob.year

    if (date.month, date.day) < (dob.month, dob.day):
        age -= 1

    print(f"You are {age} years old")

except ValueError:
    print("Invalid input")

"""
Add few days, minutes, hours, seconds, weeks to today's date
"""

new_date = date.date() + timedelta(days=10)
new_date1 = date + timedelta(hours=10, minutes=10, seconds=10, weeks=1)
print(new_date)
print(new_date1)

"""
Days until a specific date — Ask user to enter a future date and calculate days left.
"""

age_str = input("Enter any future date (dd-mm-yyyy): ")

try:
    date_frm_string = datetime.strptime(age_str, '%Y-%m-%d').date()

    if date_frm_string <= date.date():
        print('Date should be future date')
    else:
        diff = date_frm_string - date.date()
        print(f"{diff.days} days until {date_frm_string}")

except ValueError:
    print("Invalid date input")

"""
Print current time
"""

print(time.time())
print(datetime.fromtimestamp(time.time()))

"""
 Execution timer — Measure the time taken to run a loop (use time module).
"""

start_time = time.time()

for i in range(10_00_000):
    _ = i + i

end_time = time.time()
print(f"Execution took {end_time - start_time:.6f} seconds")
