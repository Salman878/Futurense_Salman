def collaz(n):
    if(n%2==0):
        print(n//2)
        return (n//2)
    else:
        print((3*n)+1)
        return ((3*n)+1)




n=int(input("enter a number"))
v=collaz(n)
s=v
while(1):
    if(s==1):
        break
    s=collaz(s)


