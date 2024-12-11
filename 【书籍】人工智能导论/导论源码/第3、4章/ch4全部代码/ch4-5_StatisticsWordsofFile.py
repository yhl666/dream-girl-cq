#ch4-5_StatisticsWordsofFile
import re   
f=open('d:\ch4_demo\test1.txt')
source=f.read()
f.close()
r='hello'
s=len(re.findall(r,source))
print(s)