inputfromuser=int(input("enter a number to make a proper triangle "))
for i in range(1,inputfromuser,2):
    for j in range((inputfromuser-i)//2):
        print(" ",end="")
    for f in range(1,i+1):
        print("*",end="")
    print("")