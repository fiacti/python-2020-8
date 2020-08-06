import random
a = 1
b = 1000
num = random.randint(a,b)
while True:
    print('the number is between%d-%d'%(a,b))
    ans = int(input('insert number:'))
    if ans<a or ans>b:
        print('the number is wrong')
    elif ans>num:          
        b = ans
    elif ans<num:
        a = ans
    elif ans==num:
        print('congrats you got it right')
        break
            



