#ch4-7_SortofText
f = open('d:\ch4_demo\test2.txt')
result = list()
for line in f.readlines():               
    line = line.strip()               
    if not len(line) or line.startswith('#'): 
        continue                 
    result.append(line)             
result.sort()                      
print(result)
open('d:/ch4_demo/test2_out.txt','w').write('%s' % '\n'.join(result)) 
