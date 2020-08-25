n = int(input())
flag = 0
n = n +1
while(flag == 0):
    a = list(map(int, str(n)))
    cnt = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i] == a[j]):
                cnt = cnt+1
    if(cnt==0):
        flag = 1
        print("".join(map(str, a)))
    else:
        flag=0
        n = n + 1
        
    
