a=[]
for i in range(0,9):
    a.append(int(input()))
b = {'1':a[0:3],'2':a[3:6],'3':a[6:9]}

c= input()
b[c].sort()
print(b[c],b[c][2],b[c][0])
