a=int(input("enter age in years:"))
if(a>0 and a<=5):
    print("toddler")
elif (a>5 and a<13):
    print("child")
elif (a>=13 and a<=19):
    print("teenager")
elif(a>19 and a<125):
    print("adult")
else:
    print("ivalid")
