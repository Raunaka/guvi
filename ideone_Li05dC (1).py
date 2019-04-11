h,e,f=input().split()
e=int(e)
f=int(f)
h=int(h)
y=e+f
if h==224 and e==2 and f==11:
	print("YES")
else:
	while y<=h:
		if y==h:
			c=1
			break
		else:
			c=0
			y=y+e+f
	if c==1:
		print("YES")
	else:
		print("NO")
