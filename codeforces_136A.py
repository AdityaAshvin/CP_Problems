n = int(input())
k = list(map(int,input().split()))
a = []
for i in range(1,len(k)+1):
    index = k.index(i)
    index = index + 1
    a.append(index)
s = " "
s = s.join(str(i)for i in a)
print(s)
    
