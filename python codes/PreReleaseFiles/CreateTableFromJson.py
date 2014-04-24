'''
Once we have all commits as json objects in a folder, we open each of them and generate file of the following format:
	File 1 : T1, T2 , T3 ...
	File 2 : t1, t2 , t3 ...
We store this in a dict object and later dump as json into a file.
'''
import requests
import json
path='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/ShaJsons/'
path2='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
f=open(path2+'sha_pre.dat','r')
f3=open('/home/pranav/Project/Eclipse2.1/CommonFiles/filelist.dat','r')
entropyfile=dict()
for x in f3:
	x=x.strip()
	entropyfile[x]=[]
	# Creates a dict object with all the file names as the key
id=0
for x in f:
	id=id+1
	str='sha'+repr(id)
	str=str.strip()	
	f2=open(path+str+'.dat','r')
	#Load each of the commit file using the sha id
	dic=json.loads(f2.read())
	#dic['files'] returns a list of dictionaries, each dictionary contains details about each file changed.
	for y in dic['files']:
		#in every dictionary, we pick just the file name.
		str=y['filename']
		wrd=str.split('/')
		list=[]
		flg=0
		for z in wrd:
			if(z=='jdt'):
				flg=1
			if(flg==1):
				if(z!='java'):
					list.append(z)
		fin='.'.join(list)
		fin=fin[:-5]
		fin=fin.strip()
		#print fin
		if fin in entropyfile.keys():'
			entropyfile[fin].append(dic['commit']['author']['date'][:10])
out2=open(path2+'outputjson.dat','w')
out2.write(json.dumps(entropyfile))
out2.close()	
			
