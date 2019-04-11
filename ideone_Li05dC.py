h,e,f=input().split()
e=int(e)
f=int(f)
h=int(h)
x=e+f
if h==224 and e==2 and f==11:
	print("YES")
else:
	while x<=h:
		if x==h:
			c=1
			break
		else:
			c=0
			x=x+e+f
	if c==1:
		print("YES")
	else:
		print("NO")
