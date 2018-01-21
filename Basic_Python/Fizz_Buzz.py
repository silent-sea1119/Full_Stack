no = int(input('Enter Number :'))

if no % 3 == 0 and no % 5 == 0:
	print 'FizzBuzz'
elif no % 3 == 0:
	print 'Fizz'
elif no % 5 == 0:
	print 'Buzz'	

