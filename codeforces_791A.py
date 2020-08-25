a,b = list(map(int,input().split()))
y = 1
flag = 0
while(flag==0):
    if(((3**y)*a)>((2**y)*b)):
        flag=1
        print(y)
    else:
        y = y+1
        flag=0
