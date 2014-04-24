import requests
import json
path='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/ShaJsons/'
path2='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/'
f=open(path2+'sha_post.dat','r')
out=f.readlines()
enter='\n'
#val and val2 are used for paralellizing. Duplicate this script and change ranges for faster commit fetches.
val=1
val2=120
ct=val
id=0
for x in out:
	id=id+1
	if(val<=id and id<val2):
		str='https://api.github.com/repos/eclipse/eclipse.jdt.core/commits/{}' .format(x)
		str=str[:-1]
		r = requests.get(str, auth=('pranavrr93', 'project1'))
		commit_data=r.json()
		filename='sha'+repr(ct)
		f=open(path+filename,'w')
		f.write(json.dumps(commit_data))	
		f.close()
		print repr(id)+' completed'
		ct+=1
	
