x=int(input())
for i in range(x):
    b=list(map(int,input().split()))
    c=sorted(b)
    print(*c,end=" ")
