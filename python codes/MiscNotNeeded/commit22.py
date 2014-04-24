import requests

f=open('sha_pre.dat','r')
out=f.readlines()
enter='\n'
ct=1
for x in out:
	str='https://api.github.com/repos/eclipse/eclipse.jdt.core/commits/{}' .format(x)
	str=str[:-1]
	r = requests.get(str, auth=('pranavrr93', 'project1'))
	commit_data=r.json()
	filename='sha'+repr(ct)
	f=open(filename,'w')
	#f.write(commit_data['commit']['message'])
	str=commit_data['commit']['message']
	buglist=str.split(" ")
	for s in buglist:
		if(s.isdigit()==True):
			f.write(s)
			f.write(enter)
			f.write(commit_data['commit']['author']['date'])
			f.write(enter)
			ct=ct+1
			for y in commit_data['files']:
				f.write(y['filename'])		
				f.write(enter)	
		

	


'''
for x in out
	ct=1
	str='https://api.github.com/repos/eclipse/eclipse.jdt.core/commits/'{}.format(x)
	r = requests.get(str, auth=('pranavrr93', 'project1'))
	#param={'since':'2003-03-27T21:30:00-05:00','until':'2004-06-25T12:08:00-04:00'})
	commit_data=r.json()
	filename='sha'+ct
	f=open(filename,'w')
	f.write()
enter='\n'
for x in commit_data:
	f.write(x['sha'])
	f.write(enter)
'''
