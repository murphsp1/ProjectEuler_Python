import sets as set


#this is a graph traversal problem



def main():
	logins = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,
689,716,731,736,729,316,729,729,710,769,290,719,680,318,
389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]

	#Deduplicating the list because duplicates are worthless
	logins = list(set.Set(logins))
	logins.sort()
	print(logins)

	logins_str = [str(l) for l in logins]
	logins_str_list = [i for i in login_str for login_str in logins_str_list ]

	print(logins_str_list)

	digits = logins[:]
	print digits





if __name__ == '__main__':
	main()