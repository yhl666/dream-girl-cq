#ch3-51_CalculationAchivement
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