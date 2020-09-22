n = int(input())
s = list(map(int,input().split()))
t = 0
m1 = max(s)
m2 = min(s)
for i in range(n):
    for j in range(0,n-i-1):
        if(s[j]<s[j+1]):
            t=t+1
            temp = s[j]
            s[j] = s[j+1]
            s[j+1] = temp
            if((s[0]==m1)and(s[n-1]==m2)):
                print(t)
                exit()

