Q=input()
if Q==Q[::-1]:
    print("yes")
else:
    a=Q.strip("0")
    
    if a==a[::-1]:
        print("yes")
    else:
        a=Q.lstrip("0")
        
        if a==a[::-1]:
            print("yes")
        else:
            print("no")