import requests as r
import os
path='/home/pranav/project/PreReleaseFiles/CommitFiles/'
os.makedirs(os.path.join(path,'UpdatedCommits'))
enter='\n'
for i in range(1,2301):
	str2='newsha'+repr(i)
	str='sha'+repr(i)
	if os.path.isfile(path+str)==False:
		continue
	f2=open(path+'UpdatedCommits/'+str2+'.dat','w')
	f=open(str,'r')
	id=1
	for x in f:
		if(id<3):
			f2.write(x)
			id=id+1
			continue
		else:
			wrd=x.split('/')
			list=[]
			flg=0
			for y in wrd:
				if(y=='jdt'):
					flg=1
				if(flg==1):
					if(y!='java'):
					#print str
						list.append(y)
			fin='.'.join(list)
			fin=fin[:-6]
			f2.write(fin)
			f2.write(enter)
			f2.close
				
			
		
