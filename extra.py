import re
mystrings = input() 
print(re.sub('\s+', ' ', mystrings).strip())
