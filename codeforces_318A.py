n,k = list(map(int,input().split()))
if(n%2==0):
    if(k>(n/2)):
        print(((k)-(n//2))*2)
    else:
        print((k*2)-1)
else:
    if(k>((n+1)/2)):
        print(((k)-((n+1)//2))*2)
    else:
        print((k*2)-1)
    
