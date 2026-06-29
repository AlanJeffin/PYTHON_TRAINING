number=list(map(int,input('enter the list:').split()))
k=int(input("Enter the threshold value k:"))
freq=dict()
for num in number:
    freq[num]=freq.get(num,0)+1
for num,count in freq.items():
    if count>k:
        print(f"{num}:{count} times")