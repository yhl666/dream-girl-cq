#ch4-6_ReplaceWordofFile
import re
f1 = open('d:\ch4_demo\test1.txt')
f2 = open('d:\ch4_demo\test1_out.txt','r+')
for s in f1.readlines():
    f2.write(s.replace('hello','hi'))
f1.close()
f2.close()