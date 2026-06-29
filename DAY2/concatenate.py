n="Harshavardhan"
half=len(n)//2
left=n[:half]
right=n[half:]
rev1=left[::-1]
rev2=right[::-1]
c=rev1+rev2
print(c)
