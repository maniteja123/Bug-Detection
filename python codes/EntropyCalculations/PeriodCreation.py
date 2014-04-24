'''
	Creates a dictionary of dictionaries. Key for first dict is the filename. Second key is the Period number, here month number (For 15months)
	We then store this into a period.dat file as a json object for entropy calculations.
'''
import datetime as dt
from datetime import timedelta
import json
# Thu, 27 Jun 2002 -- 18:35 (-0400)
date_of_rel='2002-06-27'
format = '%Y-%m-%d'
path2='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
date=dt.datetime.strptime(date_of_rel,format)
ent=dict()
f2=open(path2+'outputjson.dat','r')
dic=json.loads(f2.read())
for x in dic.keys():
	ent[x]=dict()
	for y in range(1,16):
		ent[x][y]=0

for x in dic.keys():
	for y in dic[x]:
		temp=dt.datetime.strptime(y,format)	
		difference=temp-date
		for i in range(1,16):
			if difference<timedelta(days=i*30):
				ent[x][i]+=1
				break
f=open(path2+'period.dat','w')
f.write(json.dumps(ent))
f.close()
'''		
for x in dic.keys():
	for y in dic[x]:
		temp=dt.datetime.strptime(y,format)	
		difference=temp-date
'''
		
		
