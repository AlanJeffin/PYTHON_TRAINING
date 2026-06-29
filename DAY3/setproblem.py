numbers=list(map(int,input("enter number").split()))
if len(numbers)==len(set(numbers)):
    print(False)
else:
    print(True)