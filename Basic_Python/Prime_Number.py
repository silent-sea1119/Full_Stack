no = input('Enter Number : ')
flag = 0
for x in range(2, no/2):
	if no % x == 0:
		flag = 1

if flag == 1:
	print 'Prime!!!'
else:
	print 'Not Prime!!!'
		
		
