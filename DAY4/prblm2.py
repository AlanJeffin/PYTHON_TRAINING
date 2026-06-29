N=eval(input("enter"))
sortby=input("enter sort")
def price(item):
    return item[1]
def key(item):
    return item[0]
if sortby=="price":
    N1=sorted(N,key=price)
elif sortby=="key":
    N1=sorted(N,key=key)
print(N1)
