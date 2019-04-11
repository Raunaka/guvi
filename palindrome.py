my_str = input()
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("YES")
else:
   print("NO")