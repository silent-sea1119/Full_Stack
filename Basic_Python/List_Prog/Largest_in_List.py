list = [2,11,3,4,64,12]
print 'List : ',list
min = list[0]
for i in range(1,len(list)):
	if list[i-1] < list[i]:
		min = list[i]
print 'Largest in list : ', min
