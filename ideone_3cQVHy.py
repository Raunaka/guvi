s1,s2=input().split()
n1=len(s1)
n2=len(s2)
if n2>n1:
    i=0
    while i<n1 and s1[i]==s2[i]:
        i+=1
    print(n2-i)
elif n2==n1:
    i=0
    while i<n2 and s1[i]==s2[i]:
        i+=1
    print(n2-i)
else:
    i=0
    while i<n2 and s1[i]==s2[i]:
        i+=1
    s31=s1[i:]
    s32=s2[i:]
    l=list(s31)
    k=0
    for q in s32:
        if q in l:
            k+=1
            l.remove(q)
    print(n1-i-k)
