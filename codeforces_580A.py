n = int(input())
k = list(map(int,input().split()))
cnt = 1
maxC = 0
for i in range(len(k)-1):
    if(k[i]>k[i+1]):
        if(cnt>maxC):
            maxC = cnt
        cnt = 1
    else:
        cnt=cnt+1
if(cnt>maxC):
    maxC = cnt
print(maxC)
    
