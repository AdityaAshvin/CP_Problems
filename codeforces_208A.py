s = input()
res = ""
if "WUB" in s:
    for i in range(len(s)):
        if((s[i:i+3]==("WUB"))):
            res = s.replace(s[i:i+3], ' ')
    if(res[0]==' '):
        print(res[1:])
    else:
        print(res)
else:
    print(s)
    

