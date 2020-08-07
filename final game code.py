print('Hello! What is your name?')
myname = input()

import random
a = 1
b = 1000
num = random.randint(a,b)

guesstaken = 0
while guesstaken < 100:
    print('Hello ' + myname + " ,try to guess the number, it's between %d-%d"%(a,b))
    print('insert number:')
    ans = input()
    ans = int(ans)
    guesstaken = guesstaken + 1
    if ans<a or ans>b:
        print('the number is wrong')
    elif ans>num:          
        b = ans
    elif ans<num:
        a = ans
    elif ans==num:
        
        guesstaken = str(guesstaken)
        print('congrats, you got it right, you guessed the number in ' , guesstaken ,' guesses')
        break
            