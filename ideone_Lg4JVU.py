m=input()
s=input()
m1=[]
s1=[]
r=[]
for i in m:
   m1.append(ord(i)-ord('a'))
for i in s:
   s1.append(ord(i)-ord('a'))
for i,j in zip(s1,m1):
   r.append(chr(ord('a')+(i+j)%26+1))
print("".join(r))