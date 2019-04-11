s=int(input())
n=input().split()
r=0
for i in range(0,len(n)):
   n.insert(i,int(n[i]))
   n.remove(n[i+1])
for i in range(0,len(n)-2):
   for j in range(1,len(n)-1):
      for k in range(2,len(n)):
          if(n[i]<n[j]<n[k])and(i<j<k):
             r=r+1

print(r)