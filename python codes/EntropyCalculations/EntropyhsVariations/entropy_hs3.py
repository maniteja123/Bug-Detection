import json
import math
path='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
f2=open(path+'period.dat','r')
ent=json.loads(f2.read())
values=dict()
fin=dict()
for x in ent.keys():
	n=0
	values[x]=dict()
	fin[x]=0.0
	for y in ent[x].keys():
		values[x][y]=0.0
per=dict()
for j in range(1,13):
	i=repr(j)
	sum=0.0	
	n=0
	for x in ent.keys():
		n+=ent[x][i]
	per[repr(j)]=n

for x in ent.keys():
	sum=0.0
	for y in ent[x].keys():
		if per[y]==0:
			break
		p=float(ent[x][y])/per[y]
		if p==0.0:
			values[x][y]=0.0
		else:
			values[x][y]=-p*math.log(p,2)
			sum+=values[x][y]
	fin[x]=sum
f=open(path+'entropy_hs3.dat','w')
f.write(json.dumps(fin))
	

	
		
		
	
'''		
for x in dic.keys():
	for y in dic[x]:
		temp=dt.datetime.strptime(y,format)	
		difference=temp-date
'''
		
		
