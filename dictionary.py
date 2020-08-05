import os.path

dic = {}

if not os.path.isfile('mydictionary.txt'):
    fo = open('mydictionary.txt','w')
    print('new file')
else:
    fo = open('mydictionary.txt','r')
    print('old file')

for row in fo.readlines():
    data = row.split(':')

    key = data[0]
    value = data[1]
    value = value.strip() 
    
    dic[key]=value
print(dic)

fo.close()

while True:
    print('1.vocabulary')
    print('2.print all the information')
    print('3.english to chinese')
    print('4.chinese to english')
    print('5. test')
    print('6. leave system')
    sel = input('enter option:  ')
    if sel=='1':
        en = input('enter english: ')
        ch = input('enter chinese: ')
        dic[en]=ch
    elif sel=='2':    
        for k,v in dic.items():
            print(k,':',v)
    elif sel=='3':
        search = input('search english: ')
        print(dic[search])
    elif sel=='4':
        search = input('search chinese: ')  
        for k,v in dic.items():
            if search == v:
                print(k)
    elif sel=='5':
        score=0
        for k,v in dic.items():
            print(v,':')
            ans = input('enter the answer')
            if ans==k:
                print('congrats, you got it right')
                score = score + 1
        print('your score:',score)
    elif sel=='6':
        break         
         