def check():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    
    if(a>b):
        print(a)
    elif(b>a):
        print(b)
    elif(a==b):
        print(a,"and",b,"are equal")
check()
