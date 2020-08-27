a = int(input())
b = int(input())
c = int(input())
s = 0
if((a==1)and(b!=1)and(c!=1)):
    s = (a+b)*c
elif((a==1)and(c==1)):
    s = a+b+c
elif((a==1)and(b==1)and(c!=1)):
    s = (a+b)*c
elif((a!=1)and(b==1)and(c==1)):
    s = a*(b+c)
elif((a!=1)and(b!=1)and(c==1)):
    s = a*(b+c)
elif((a!=1)and(b==1)and(c!=1)):
    if(a>c):
        s = a*(b+c)
    else:
       s = (a+b)*c
else:
    s = a*b*c
print(s)
