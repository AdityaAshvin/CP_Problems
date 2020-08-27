n = int(input())
arr = []
if(n>1):
    for i in range(1,n):
        if(i%2==0):
            arr.append("I love that")
        else:
            arr.append("I hate that")
    if((n-1)%2==0):
        arr.append("I hate it")
    else:
        arr.append("I love it")
    s = " "
    s = s.join(arr)
    print(s)
else:
    print("I hate it")
