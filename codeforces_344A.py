n = int(input())
arr = []
cnt = 0
if(n>1):
    for i in range(n):
        a = int(input())
        arr.append(a)
    for i in range(len(arr)-1):
        if(arr[i]==arr[i+1]):
            cnt = cnt
        else:
            cnt = cnt+1
    print(cnt+1)
else:
    print("1")
    
