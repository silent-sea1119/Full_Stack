dictx = {"Rollno":17, "Name" : "Akshay", "Class" : "BE-B"}
dicty = {"Rollno":17, "Name" : "Akshay", "Class" : "BE-B"}
dictz = {"Rollno":69, "Name" : "Kundan", "Class" : "BE-B"}
dicta = {"Rollno":1, "Name" : "Z", "Class" : "BE-B"}

print 'str	: ',str(dictx)
print 'len	: ',len(dictx)
print 'type	: ', type(dictx)
print 'get	: ',dictx.get('Name', 'not_found')
print 'Compare_xy	:',cmp(dictx, dicty)
print 'Compare_xz	:',cmp(dictx, dictz)
print 'Compare_ax	:',cmp( dicta,dictx)

seq = ['name','rollno','class']
print seq
dic = dict.fromkeys(seq)
print 'fromkeys seq : ',dic
dic.clear()
print 'clear dict : ',dic
dic = dict.fromkeys(seq, 'Vishal')
print 'fromkeys seq,value : ',dic

print 'has_key : ',dictx.has_key('Name')
print 'items() : ',dictx.items()
print 'keys : ',dictx.keys();

