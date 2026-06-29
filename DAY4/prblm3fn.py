day=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
d=input("enter day")
amount=int(input("enter amount"))
def party(day,amount):
    if day in ("Mon","Tue","Wed","Thu") and 700<amount<=1000 or day in ("Fri","Sat","Sun") and 1000<amount<1500:
        return "party succesfull"
    else:
        return "party unsucessfull"
print(party(d,amount))
    
        
    