s = ["101", "102", "103", "104", "102", "105", "106", "103"]
#s=input("enter:").split()
#s = ["abc", "def", "abc", "xyz"]
d={}
result=set()
for i in s:
    d[i]=d.get(i, 0) + 1

for key in d:
    if d[key]==1:
        result.add(key)
print(result)