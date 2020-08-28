n, m = list(map(int,input().split()))
f = list(map(int,input().split()))
f.sort()
best = 1000
if(len(f)==2):
    print(f[1]-f[0])
    exit()
else:
    for i in range((m-n)+1):
      best = min(best, f[i+n-1] - f[i])
print(best)
