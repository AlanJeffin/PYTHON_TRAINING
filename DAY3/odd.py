num=input("Enter number")
even=0
odd=0
digit_list = [int(digit) for digit in str(num)]
for i in range(len(digit_list)):
    if digit_list[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
        