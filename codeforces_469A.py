n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = []
arr = a+b
print(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)-1):
        if(arr[i]==arr[j]):
            arr.remove(arr[j])
print(arr)
if(len(arr)==n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
