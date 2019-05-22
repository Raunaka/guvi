import string
def ispangram(st):
    small=set(string.ascii_lowercase)
    return small<=set(st.lower())

a=input()
if ispangram(a):
    print('yes')
else:
    print('no')
    