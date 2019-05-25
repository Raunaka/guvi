a=input()
a=list(a)
if a==a[::-1]:
	while a==a[::-1]:
		a[-1]=""
q=""
for i in a:
	q=q+i
print(q)
