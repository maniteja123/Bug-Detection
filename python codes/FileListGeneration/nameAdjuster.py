'''
	This code takes in an input file and converts the file format to a suitable form, for 
	java,  it is jde.core...... 
'''
f=open('/home/pranav/Project/Eclipse2.1/CommonFiles/filelist.dat','r')
f2=open('/home/pranav/Project/Eclipse2.1/CommonFiles/newfile.dat','w')
enter='\n'
for c in f:
	list=c.split('/')
	wrd=[]
	flg=0
	for str in list:
		if(str=='jdt'):
			flg=1
		if(flg==1):
			if(str!='java'):
				#print str
				wrd.append(str)
	filename='.'.join(wrd)
	filename=filename[:-6]
	f2.write(filename)
	f2.write(enter)
f2.close()

		
