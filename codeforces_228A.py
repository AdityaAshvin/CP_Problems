s = list(map(int,input().split()))
cnt=0
arr=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            arr.append(s[i])
            break;
print(len(arr))
