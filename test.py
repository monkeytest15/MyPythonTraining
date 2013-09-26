import datetime, calendar

lastFriday = datetime.date.today()
oneday =datetime.timedelta(days=1)
while lastFriday.weekday() != calendar.FRIDAY:
	lastFriday -=oneday
print lastFriday.strftime('%A, %d-%b-%Y')