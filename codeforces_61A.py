a = input()
b = input()
arr = []
for i in range(len(a)):
    c = (int(a[i]) ^ (int(b[i])))
    arr.append(c)
print("".join(map(str,arr)))
    

