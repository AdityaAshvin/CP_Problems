n = int(input())
k = list(map(int,input().split()))
cnt = 0
for i in k:
    if(i == 1):
        cnt = cnt+1
    else:
        cnt = cnt
if(cnt!=0):
    print("HARD")
else:
    print("EASY")
