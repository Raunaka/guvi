s12,s22=input().split()
s=0
if len(s12)>len(s22):
    s12,s22=s22,s12
k=0
while k<len(s12):
    s+=(ord(s22[k])-ord(s12[k]))
    k+=1
for k in range(k,len(s22)):
    s+=ord(s22[k])-ord('a')+1
print(s)