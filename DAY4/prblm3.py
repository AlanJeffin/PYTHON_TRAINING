day=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
d=input("enter day")
n=int(input("enter"))
if d in ("Mon","Tue","Wed","Thu") and 700<n<=1000 or d in ("Fri","Sat","Sun") and 1000<n<1500:
    print("party successfull")
else:
    print("party unsuccessfull")


    


