N=input('enter number')
increasing=True
decreasing=True
for i in range(len(N)-1):
    if int(N[i+1]!=int(N[i])+1):
        increasing=False
    if int(N[i+1]!=int(N[i])-1):
        increasing=False
if increasing==True:
    print("fancy")
elif decreasing==True:
    print("fancy")
else:
    print("not fancy")