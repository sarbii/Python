f1 = open('text.txt' ,'w')
for i in range(1,10):
    data = '%d lines\n' %i
    f1.write(data)
f1.close()

f2 = open('text.txt','r')

a=int(input())
f2.seek((a-1)*8,0)#������������ 8�̶� ����� 2lines�� ��µ� �����쿡�� 8�� �Է��ϸ� ���� ��µ�
data = f2.readline()
print(data)