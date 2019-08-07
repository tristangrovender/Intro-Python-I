"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

if len(sys.argv) == 1:
  m = datetime.now().month
  y = datetime.now().year

elif len(sys.argv) == 2:
  if sys.argv[1].isdigit() and len(sys.argv[1]) == 2:
    m = int(sys.argv[1])
    y = datetime.now().year
  else:
    print("Enter the month as a 2 digit argument")
    exit()
elif len(sys.argv) == 3:
  if sys.argv[1].isdigit() and sys.argv[2][1:5].isdigit():
    m = int(sys.argv[1])
    y = int(sys.argv[2][1:5])
  else:
    print("enter date in format MM [YYYY]") 
    exit() 

print(calendar.month(y, m))
print(calendar.month(14, 5))