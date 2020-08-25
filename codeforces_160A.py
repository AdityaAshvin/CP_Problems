n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
s = 0
max = sum(a)
for i in range(len(a)):
    s = s + a[i]
    if(s>(max/2)):
        print(i+1)
        break
