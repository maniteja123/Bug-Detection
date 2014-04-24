import requests as r
import os

path='/home/karthik/github/mining/'
path1='/home/karthik/thesis/graph/dataset/jdt-core-3.0'
def main():
    try:
        os.makedirs(os.path.join(path,'commits'))
    except Exception as ex:
        if ex[1]=='File exists':
            print ex[1]
    files=dict()
    f1=open(os.path.join(path1,'bugs_cycle.csv'),'r') #similar to ur filenames extracted from the source code
    #f1=open('~/thesis/graph/dataset/jdt-core-3.0/bugs_cycle.csv','r')
    for line in f1:
        if line.startswith('jdt'):
            name=line.split(',')[0]
            #assert (name in files.keys()),'duplicate entry'
            if name in files.keys():
                assert 1,'duplicate key'
            files[name]=0
    f1.close()
    f=open(os.path.join(path,'shalist.dat'),'r')
    count_line=0
    count_maps=0
    for line in f:
        sha=line.strip()
        l=r.get('https://api.github.com/repos/eclipse/eclipse.jdt.core/commits/{}'.format(sha),auth=('karthikbox','Shampoo1@'))
        commit_files=l.json()['files']
        count_files=0
        for commit_file in commit_files:
            str=[]
            print commit_file['filename']
            #converting commit filenames into the format of names in bugs_cycles.csv
            if commit_file['filename'].split('/')[0]=='org.eclipse.jdt.core':
                comps=commit_file['filename'].split('/')
                comps.reverse()
                if not comps[0].endswith('.java'):
                    print '^skip because not .java'
                    continue
                for c in comps:
                    if c.endswith('.java'):
                        str.append(c.split('.')[0])
                    else:
                        str.append(c)
                        if c=='jdt':
                            break
                str.reverse()
                if '.'.join(str) not in files.keys():
                    print '.'.join(str)
                    print '^skip because this file not in our previous keys'
                    continue
                else:
                    count_maps+=1
                    files['.'.join(str)]+=1
                    print '.'.join(str)
            else:
                print '^skip because not org.eclipse.jdt.core'
                pass
        count_line+=1
        print '^ count_line count_maps',count_line,count_maps
        #raw_input('>')
    f.close()
    f=open(os.path.join(path,'changes.csv'),'w')
    for k in files.keys():
        f.write('{},{}\n'.format(k,files[k]))
    f.close()
    #print files.items()
                            

if __name__=='__main__':
    print 'main running'
    main()
else:
    print 'main imported'
