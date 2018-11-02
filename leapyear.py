import calendar
# print calendar.isleap(2014)
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 1is a leap year".format(year))
       else:
           print("{0} 1is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
   print("Closest leap year is"+str(year-1))

