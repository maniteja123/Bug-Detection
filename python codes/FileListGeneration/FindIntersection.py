'''
	This program reads from two files, stores the files in two separate lists and finds the common files and inserts into a third file
'''
path='/home/pranav/Project/Eclipse2.1/CommonFiles/'
f1=open(path+'list2.dat','r')
f2=open(path+'list21.dat','r')
f3=open(path+'list_intersection.dat','w')
list1=[]
list2=[]
for line in f1:
	list1.append(line)
	#print line
for line in f2:
	list2.append(line)
	#print line
inter=list(set(list1)&set(list2))
for x in inter:
	print x
	f3.write(x)


