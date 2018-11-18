a= input()
b= input()

c= set(a).union(b)-set(a).intersection(b)
e=list(c)
e.sort()
f= e

print(f)