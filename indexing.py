n,q = map(int,input().split())
lis = list(map(int,input().split()))
str1 = ""
for i in range(q):
    u,v = map(int,input().split())
    ans  = sum(lis[u-1:v])
    if(i == 0):
        str1 = str1+str(ans)
    else:
        str1 = str1+"\n"+str(ans)
print(str1)
