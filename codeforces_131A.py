s = input()
a = s[1:len(s)]
if(len(s)==1):
    if(s.isupper()):
        print(s.lower())
    else:
        print(s.upper())
    exit()
if(s.isupper()):
    print(s.lower())
    exit()
elif(a.isupper()):
    a = a.lower()
    f = str(s[0])+a
    print(f.capitalize())
    exit()
print(s)

