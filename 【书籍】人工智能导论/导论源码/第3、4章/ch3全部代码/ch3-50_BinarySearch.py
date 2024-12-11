#ch3-50_BinarySearch
from random import randint
def binarySearch(lst, value):
    start = 0
    end = len(lst)
    while start < end:         
        middle = (start + end) // 2           
        if value == lst[middle]:         
            return middle        
        elif value > lst[middle]:       
            start = middle + 1        
        elif value < lst[middle]:        
            end = middle - 1    
    return False                          
lst = [randint(1,50) for i in range(20)]
lst.sort()
print(lst)
result = binarySearch(lst, 30)
if result!=False:
    print('Success, its position is:',result)
else:
    print('Fail. Not exist.')
while True:
    try:
        n = int(input('请输入评委人数：'))
        if n <= 2:
            print('评委人数太少,必须多于2个人。')
        else:
            break 
    except:
        pass
scores=[]
for i in range(n):
    score = input('请输入第{0}个评委的分数：'.format(i+1))
    score = float(score)
    scores.append(score)           
highest = max(scores)
lowest = min(scores)
scores.remove(highest)
scores.remove(lowest)
finalScore = round(sum(scores)/len(scores), 2)
formatter = '去掉一个最高分{0}\n去掉一个最低分{1}\n最后得分{2}'
print(formatter.format(highest, lowest, finalScore))