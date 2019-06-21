a=input()
v=''
w=[]
for i in a:
    if i not in w:
        v+=i
        w.append(i)
    elif i in w:
        break
print(len(w))
