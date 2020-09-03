n = int(input())
p = list(map(int,input().split()))
x = 10
v1 = 0
for i in range(len(p)):
    v1 = v1 + ((x * p[i])/100)
v2 = n * x
totalV = v1/v2
print(totalV*100)
