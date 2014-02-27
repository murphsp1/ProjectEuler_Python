#Counting Sundays

import calendar

def main():

	years = xrange(1901, 2001)
	months = xrange(1,13)

	count = 0
	for y in years:
		for m in months:
			days = [calendar.weekday(y,m,d+1) for d in range(calendar.mdays[m])]
			
			if days[0]==6:
				count += 1
				print(m,y)


	print(count)

if __name__ == ('__main__'):
	main()