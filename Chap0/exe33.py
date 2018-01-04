
def april(i): 
	numbers = []
	while i < 6:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d " % i 
		
	print "the numbers: "

	for number in numbers:
		print number

print april(7)