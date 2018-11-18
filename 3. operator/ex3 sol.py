l1={'a':7,'b':9,'c':11,'d':13,'e':3,'f':20,'g':5,'h':30,'i':2,'j':5}
q=input()
w=0
for i in range(0,len(q)):
    w += l1[q[i]]
r=(int)(round(w/len(q)+0.5))
print(r)