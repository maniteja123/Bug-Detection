'''
	This script reads all the commit data using first api, looks at the message field and checks if bug fix id matches any 
	of the bug id's that were reported in 1 year. If match is found, we store the sha value in sha_post.
'''
import requests
'2003-03-27 21:30:00'
l = requests.get('https://api.github.com/repos/eclipse/eclipse.jdt.core/commits', auth=('karthikbox', 'Shampoo1@'),params={'since':'2003-03-27T21:30:00-04:00','until':'2005-03-27T21:30:00-04:00'})
commit_data=l.json()
path='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/'
f2=open(path+'bugz_time.dat','r')
bugid=f2.read()
enter='\n'
f=open(path+'sha_post.dat','w')
id=0
print 'batch {} of size {}'.format(id,len(commit_data))
id=id+1
for x in commit_data:	
	str=x['commit']['message']
	buglist=str.split(" ")
	for s in buglist:	
		s=s.strip()
		#Better technique can be used to spot numbers in message field.
		if(s.isdigit()==True):
			if s in bugid:
				print 'printing sha to file'
				print x['sha']
				print ' '
				f.write(x['sha'])	 
				f.write(enter)

import re
pat=re.compile(',|;')
#For pagination 

while True:
	if len(pat.split(l.headers['link']))==2: break
    	l=requests.get(pat.split(l.headers['link'])[0].strip('<>'),auth=('pranavrr93','project1'))
    	#print l.headers['link']
    	commit_data=l.json()
	print 'batch {} of size {}'.format(id,len(commit_data))
	id=id+1
	for x in commit_data:	
		str=x['commit']['message']
		buglist=str.split(" ")
		for s in buglist:
			s=s.strip()
			if(s.isdigit()==True):
				if s in bugid:
					print 'printing sha to file'
					print x['sha']
					print ' '
					f.write(x['sha'])	 
					f.write(enter)
f.close()
f2.close()

# End of script

