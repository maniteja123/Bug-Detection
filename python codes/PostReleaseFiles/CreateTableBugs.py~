'''
	This file generates the Entropy Table, i.e, each file along with the number of bugs found in it.Our final goal for the Post Version Phase.
'''
import requests
import json
path='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/ShaJsons/'
path2='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/'
path3='/home/pranav/Project/Eclipse2.1/CommonFiles/'
f=open(path2+'sha_post.dat','r')
f3=open(path3+'filelist.dat','r')
entropyfile=dict()
for x in f3:
	x=x.strip()
	entropyfile[x]=0
	#Dict with each file name as the key
id=0
for x in f:
	id=id+1
	str='sha'+repr(id)
	str=str.strip()	
	f2=open(path+str,'r')
	dic=json.loads(f2.read())
	#dic['files'] returns a list of dictionaries, each dictionary contains details about each file changed.
	for y in dic['files']:
		#in every dictionary, we pick just the file name.
		str=y['filename']
		wrd=str.split('/')
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
		fin=fin[:-5]
		fin=fin.strip()
		#print fin
		if fin in entropyfile.keys():
			entropyfile[fin]+=1
			#increment number of bugs by 1
out2=open(path2+'output_post_list.dat','w')
enter='\n'
out2.write(json.dumps(entropyfile))
'''
for x in entropyfile.keys():
	out2.write(x)
	out2.write(' ')
	out2.write(repr(entropyfile[x]))
	out2.write(enter)
out2.close()
'''

	
			
