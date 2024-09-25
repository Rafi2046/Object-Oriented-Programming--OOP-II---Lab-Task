#Python program to display calendar

import calendar
yy = int(input("Enter Year: "))
mm = int(input("Enter Month: "))

print(calendar.month(yy,mm))
