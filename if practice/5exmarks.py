mark=int(input("enter marks obtained:"))

if (mark>35 and mark<60):
    print ("average")
elif(mark<=100 and mark>=90):
    print("A")
elif (mark<=89 and mark>=80):
    print("B")
elif (mark<=79 and mark>=60):
    print("C")
elif (mark<=69 and mark>=59):
    print("D")
elif (mark<35):
    print("fail")
else:
    print("unsupported value")
