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
        n = int(input('��������ί������'))
        if n <= 2:
            print('��ί����̫��,�������2���ˡ�')
        else:
            break 
    except:
        pass
scores=[]
for i in range(n):
    score = input('�������{0}����ί�ķ�����'.format(i+1))
    score = float(score)
    scores.append(score)           
highest = max(scores)
lowest = min(scores)
scores.remove(highest)
scores.remove(lowest)
finalScore = round(sum(scores)/len(scores), 2)
formatter = 'ȥ��һ����߷�{0}\nȥ��һ����ͷ�{1}\n���÷�{2}'
print(formatter.format(highest, lowest, finalScore))