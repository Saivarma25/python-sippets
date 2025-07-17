"""
Script to check given year is a leap year
"""

def check_leap_year(year):
    if year%4 == 0 and year%100 != 0:
        return True
    if year%400 == 0:
        return True
    return False

if __name__ == "__main__":
    year_str = input("Enter any year: ")
    if year_str.isdigit():
        print(check_leap_year(int(year_str)))
    else:
        print("Pleas enter valid year")