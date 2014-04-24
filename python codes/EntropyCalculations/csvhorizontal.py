import json
ent=dict()
path='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
path2='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/'

f=open(path+'entropy_hs.dat','r')
ent['1']=dict()
ent['1']=json.loads(f.read())

f=open(path+'entropy_hs1.dat','r')
ent['2']=dict()
ent['2']=json.loads(f.read())

f=open(path+'entropy_hs2.dat','r')
ent['3']=dict()
ent['3']=json.loads(f.read())

f=open(path+'entropy_hs3.dat','r')
ent['4']=dict()
ent['4']=json.loads(f.read())

f=open(path2+'output_post.dat','r')
ent['5']=dict()
ent['5']=json.loads(f.read())

f=open(path+'final_output_hs','w')
str='filename,entropyhs,entropyhs1,entropyhs2,entropyhs3,bugs'
comma=','
enter='\n'
f.write(str)
f.write(enter)
for x in ent['1'].keys():
	f.write(x)
	f.write(comma)
	for y in ent.keys():
		#print ent[y][x]
		f.write(repr(ent[y][x]))
		f.write(comma)
	f.write(enter)
f.close()
		

