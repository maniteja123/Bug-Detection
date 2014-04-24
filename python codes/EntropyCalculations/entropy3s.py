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
for j in range(1,16):
	i=repr(j)
	sum=0.0	
	n=0
	for x in ent.keys():
		n+=ent[x][i]
	for x in ent.keys():
		if n==0:
			break
		p=float(ent[x][i])/n
		if p==0.0:
			values[x][i]=0.0
		else:
			values[x][i]=-p*math.log(p,2)
			sum+=values[x][i]
			sum=sum/n
	for x in ent.keys():
		if values[x][i]==0.0:
			continue
		else:
			values[x][i]=sum/math.log(n,2)

for x in ent.keys():
	for y in ent[x].keys():
		fin[x]+=values[x][y]
f=open(path+'entropy3s.dat','w')
f.write(json.dumps(fin))	
		
		
	
'''		
for x in dic.keys():
	for y in dic[x]:
		temp=dt.datetime.strptime(y,format)	
		difference=temp-date
'''
		
		
