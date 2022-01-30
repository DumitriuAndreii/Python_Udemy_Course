# function with outputs

# def format_name(f_name,l_name):
#     if f_name =="" or l_name == "":
#         return "You didn't provide valid inputs"
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name},{formatted_l_name}"
#
# print(format_name("ANDREI", ""))

# Ex1 - is leap year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]
# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)