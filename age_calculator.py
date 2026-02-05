import datetime as dt
from dateutil.relativedelta import relativedelta

DOB = input('Your Date Of Birth: ')
DOB2 = dt.date.strptime(DOB, "%d %B %Y")
print(DOB2)

today = dt.date.today()

diff = relativedelta(today, DOB2)

Years = diff.years
months = diff.months
days = diff.days

print('Your age is:', f'{Years} years {months} months {days} days')

if(
 today.month == DOB2.month
 and today.day >= DOB2.day
or today.month > DOB2.month):
    nextBirthdayYear = today.year + 1
else:
    nextBirthdayYear = today.year

nextBirthday = dt.date(nextBirthdayYear, DOB2.month, DOB2.day)
nextbirthday = nextBirthday.strftime('%A, %d %B %Y')
print('Your next Birthday is on:', nextbirthday)

diffe = nextBirthday - today
print('Number of days left for Birthday:',diffe.days,'days')


