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

def days_in_month(year_param, month_param):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if month_param > 12 or month_param < 1:
        return "invalid input, please type an integer between 1-12"
    for months in month_days:
        if is_leap(year) and month_param == 2:
            return 29
        return month_days[month_param - 1]
 
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












