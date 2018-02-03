no = input("Enter Number 1 : ")
no1 = input("Enter Number 2 : ")

def smallest(no,no1):
	if no<no1:
		return no
	else:
		return no1 

flag = 0
for i in range(2, smallest(no,no1)):
	if (no%i == 0 and no1%i == 0):
		print 'LCM : ', i
		flag = 1
		break
if flag == 0:
	print 'No LCM'
