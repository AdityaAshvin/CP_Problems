y,b,r=input().split()
y=int(y)
b=int(b)
r=int(r)
if y<b<r :
    print(y+y+1+y+2)
if y>b<r and r!=y:
    print(b-1+b+1+b)
if y<b>r and (r-1==y or y>r):
    print(r+r-1+r-2)
if y==b==r:
    print(y+y-1+y-2)
if y==b>r:
    print(r-1+r+r-2)
if y==r>b:
    print(b-1+b+b+1)
if y>b==r:
    print(b-1+b-2+b)
if y<b>r and y<r and r-1!=y:
    print(y+2+y+1+y)
if r==y<b:
    print(y-1+y-2+y)
if r==b>y and y+1!=r:
    print(y+y+1+y+2)
if y==b<r:
    print(y-1+y+y+1)
if r==b>y and y+1==r:
    print(r+r+r-1-2)
