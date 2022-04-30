def strip(string,ch):
    new=string[:]
    for i in new[0::]:
        if i==ch:
            new=new.replace(i,'')
    for i in new[-1::-1]:
        if i==ch:
            new = new.replace(i, '')
    return new












string = input("enter your string")
v=strip(string,'!')
print(v)