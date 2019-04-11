num=int(input())
stepss=list(map(int,input().split()))
total=0
for i in range(1,len(stepss)):
	     for j in range(0,i):  
		           if(stepss[j]<stepss[i]):
			                 total+=stepss[j]
print(total)
