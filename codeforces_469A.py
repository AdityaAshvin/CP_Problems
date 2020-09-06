n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = []
arr = a+b
for i in range(len(arr)-1):
    for j in range(i,len(arr)-2):
        if(arr[i]==arr[j]):
            arr.remove(arr[j])
if(len(arr)==n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
