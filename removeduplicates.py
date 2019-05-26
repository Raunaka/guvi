from collections import OrderedDict
def removeduplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))
     
print(removeduplicate(input()))
