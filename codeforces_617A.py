n=int(input())
t=0
if n>=5:
 if n%5==0:   
  t=n//5
 else:
     t=n//5+1
if n<5:
 t=1
print(t)
