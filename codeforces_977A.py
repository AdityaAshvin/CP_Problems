n,k = list(map(int,input().split()))
i = 0
while(i<k):
    l = n%10
    if(l == 0):
        n = n//10
    else:
        n = n - 1
    i = i+1
print(n)
    
