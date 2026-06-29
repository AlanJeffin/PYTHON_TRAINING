a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=int(input("enter d"))
if a>b and a>c and a>d:
    print("a largest")
elif b>a and b>c and b>d:
    print("b largest")
elif c>a and c>b and c>d:
    print("c largest")
else:
    print("d largest")
