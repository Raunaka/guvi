q=input()
b=0
c=[]
for i in range(0,len(q)-1):
    for j in range(i+1,len(q)):
        k=q[i:j+1]
        l=k[::-1]
        if k==l:
            c.append(len(q)-len(l))
print(min(c))
