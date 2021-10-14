a=input()
for i in a:
    if i.upper():
        i=i.lower()
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="y":
            print(end="")
        else:
            print(".",end="")
            print(i,end="")
