c=int(input())
b=int(input())
sum = 0
while (b!=0):
    remainder = b%10
    sum += remainder
    b = b//10
print(sum)