'''
	Reads from sha values file and requests server for the complete info about that commit. We fetch it as a 
	dict object and dump it in a .dat file as a json object. 
'''

import requests
import json
path='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
path2='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/ShaJsons/'
f=open(path+'sha_pre.dat','r')
out=f.readlines()
enter='\n'
id=0
val1=1860	
val2=1904
#2001-2250
for x in out:
	id+=1
	if(id<=val1 or id>=val2):
		continue
	str='https://api.github.com/repos/eclipse/eclipse.jdt.core/commits/{}' .format(x)
	str=str[:-1]
	r = requests.get(str,auth=('karthikbox','Shampoo1@'))
	commit_data=r.json()
	filename='sha'+repr(id)
	f=open(path2+filename+'.dat','w')
	f.write(json.dumps(commit_data))	
	#json.dump(commit_data,f)
	f.close()
	print repr(id)+' completed'

	

	
