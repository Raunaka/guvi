n=int(input())
a=input().split(' ')
b= [int(i) for i in a]
b.sort()
n=int(n/2)
print(b[n])
