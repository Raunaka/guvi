K=input()
K=int(K)
l=[]
for i in range(0,K):
    s=input()
    l.append(s)
common_prefix=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
        common_prefix.append(i[0])
    else:
        break
ans=''.join(common_prefix)
print(ans)
