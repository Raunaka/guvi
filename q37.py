n3 = int(input())
L = [ int(x) for x in input().split()]
n3 = len(L)
if n3==1 :
    print(1)
   
cnt = 0
for i in range(1,n3-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        cnt += 1
print(cnt)
