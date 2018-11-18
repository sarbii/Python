x = int(input())

big=0
small =0

if((x%10)>5):
    big = (x//10) +1
    small = 0
else:
    big = x//10
    small = 1


print(big)
print(small)
print(big*8 + small*5 + x)