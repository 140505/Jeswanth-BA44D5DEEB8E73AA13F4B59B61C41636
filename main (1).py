def isLeapYear(year):
  if(year% 4==0 and year % 100!=0) or year % 400==0:
    return true
  else:
    return false
year=int(input("enter a year:"))
if isLeapyear(year):
  print("{} is leapyear.".format(year))
else:
  print("{} is not leapyear.". format (year))
