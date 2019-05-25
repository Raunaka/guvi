a=int(input())
for i in range(a):
    list1=list(map(int,input().split()))
    q='>-'
    w=q.join(map(str,list1))
    print(w[::-1],end='')
    break
    print(end='')
