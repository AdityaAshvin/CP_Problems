n, h = list(map(int,input().split()))
a = list(map(int,input().split()))
cnt = 0
for i in a:
    if(i>h):
        cnt = cnt+2
    else:
        cnt = cnt+1
print(cnt)
