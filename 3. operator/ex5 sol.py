import random

#l1={'1':'scisssor','2':'rock','3':'paper'}
l1=['','scisssor','rock','paper']
l2=[1,2,3]

i=0
while i!=2:
    b = random.choice(l2)
    a = int(input())
    c = 4 * a + b

    print(l1[a])
    print(l1[b])
    if(a==b):
        print('사용자 무승부')
    elif(c==7 or c==9 or c==14):
        print('사용자 승')
        i += 1
    else:
        print('사용자 패')
