import math
n=int(input())
k=[]
while n%2==0:
    k.append(2)
    n=n/2
for i in range(3,(int(math.sqrt(n))+1),2):
        if n%i==0:
            k.append(i)
            n=n/i
if n>2:
   k.append(int(n))  
k=list(set(k))          
for i in range((len(k)-1)):
   print(k[i],end=' ')
print(k[(len(k)-1)],end='')   
      