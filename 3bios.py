def jumbled_letters():

    z=int(input("Enter the number of test cases: "))

    for k in range(z):

        a= str(input("Enter the sentence: "))
        b=str(a.replace(" ", ""))

        c = len(b)
        s1=[]

        ochar=[]
        echar=[]

        for i in  range(0,c):
            if i%2==0:
                echar.append(b[i])
            else:
                ochar.append(b[i])

        s1.append(ochar[::-1])

        f1=[]
        for sublist in s1:
            for items in sublist:
                f1.append(items)


        ea=str("".join(echar))
        oa=str("".join(f1))
        print(ea+oa)

if __name__ == "__main__":
    jumbled_letters()
