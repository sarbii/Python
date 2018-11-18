x=int(input())
y=int(input())


a=4*x
b=4*y

c=str(bin(a&b))
d=str(bin(a|b))

print(c.count('1'))

print(d.count('1'))