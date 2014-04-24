import json
ent=dict()
path='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
path2='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/'
f=open(path+'entropy1s.dat','r')
ent['1']=dict()
ent['1']=json.loads(f.read())


f=open(path+'entropy2s.dat','r')
ent['2']=dict()
ent['2']=json.loads(f.read())

f=open(path+'entropy3s.dat','r')
ent['3']=dict()
ent['3']=json.loads(f.read())

f=open(path+'entropy1d.dat','r')
ent['4']=dict()
ent['4']=json.loads(f.read())

f=open(path+'entropy2d.dat','r')
ent['5']=dict()
ent['5']=json.loads(f.read())

f=open(path+'entropy3d.dat','r')
ent['6']=dict()
ent['6']=json.loads(f.read())

f=open(path+'entropy_hs.dat','r')
ent['7']=dict()
ent['7']=json.loads(f.read())

f=open(path+'entropy_hd.dat','r')
ent['8']=dict()
ent['8']=json.loads(f.read())

f=open(path2+'output_post.dat','r')
ent['9']=dict()
ent['9']=json.loads(f.read())
f3=open(path+'allent.dat','w')
f3.write(json.dumps(ent))
f=open(path+'final_output','w')
str='filename,entropy1s,entropy2s,entropy3s,entropy1d,entropy2d,entropy3d,entropyhs,entropyhd,bugs'
comma=','
enter='\n'
f.write(str)
f.write(enter)
for x in ent['1'].keys():
	f.write(x)
	f.write(comma)
	for y in range(1,10):
		z=repr(y)
		#print ent[y][x]
		f.write(repr(ent[z][x]))
		f.write(comma)
	f.write(enter)
f.close()
		

