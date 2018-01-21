# Reverse given integer number < 1000

no = input('Enter Number : ')
if no <= 99:
	x = str(no % 10);
	x += str(int(no/10));
	print x

elif no >= 100 and no <= 999:
	x = str((no%100)%10)
	x += str((no%100)/10)
	x += str(no/100)
	print x

	
