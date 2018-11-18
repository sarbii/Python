x = int(input())

y = int(input())

z = "    "
a=y
for i in range(x, 0, -1):


    print()
    print(z * (a+x-y-1), end='')
    y += 1
    for j in range(1, y-x+1):

        print("%4d" %(i*100+j), end='')