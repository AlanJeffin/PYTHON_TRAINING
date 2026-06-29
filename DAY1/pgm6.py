n=int(input("enter rain in mm"))
if 0<=n<=1:
    print("no rain")
elif 2<=n<=5:
    print("light rain")
elif 5<=n<=10:
    print("moderate rain")
else:
    print('heavy rain')