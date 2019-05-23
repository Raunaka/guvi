a=int(input())
length=len(str(a))
sum=0
temp=a
while(temp!=0):
    sum=sum+((temp%10)**length)
    temp=temp//10
if sum==a:
    print('yes')
else:
    print('no')