#ch3-47_GuessofNumber
from random import randint
def guess(maxValue=100, maxTimes=5):
    value = randint(1,maxValue)     
    for i in range(maxTimes):
        prompt = 'Start to GUESS:' if i==0 else 'Guess again:'
        try:
            x = int(input(prompt))
        except:
            print('Must input an integer between 1 and ', maxValue)
        else:
            if x == value:                      
                print('Congratulations!')
                break
            elif x > value:
                    print('Too big')
            else:
                 print('Too little')   
guess(98£¬34)
def  Rate(origin, userInput):
    if not (isinstance(origin, str) and isinstance(userInput, str)):
        print('The two parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry. I suppose the second parameter string is shorter.')    
        return
    right = 0                  
    for origin_char, user_char in zip(origin, userInput):
        if origin_char==user_char:
            right += 1
    return right/len(origin)
origin = 'Shandong Institute of Business and Technology'
userInput = 'ShanDong institute of business and technolog'
print(Rate(origin, userInput)) 