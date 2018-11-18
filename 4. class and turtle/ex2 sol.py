f1 = open('text.txt' ,'w')
for i in range(1,10):
    data = '%d lines\n' %i
    f1.write(data)
f1.close()

f2 = open('text.txt','r')

a=int(input())
f2.seek((a-1)*8,0)#리눅스에서는 8이라 해줘야 2lines가 출력됨 윈도우에서 8로 입력하면 개행 출력됨
data = f2.readline()
print(data)