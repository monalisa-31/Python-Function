def calculator():
    a=int(input("enter a num"))
    b=int(input("enter a num"))       
    c=(input("enter a symbol"))
    if c=="+":
        d=a+b
        return d
    elif c=="-":
        e=a-b
        return e
    elif c=="*":
        f=a*b
        return f
    elif c=="%":
        g=a%b
        return g
    else:
        pass   
print(calculator())