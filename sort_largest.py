a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    d=sorted(b)
    print(d[-1],end=" ")
