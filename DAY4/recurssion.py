def mcCarthy91(num):
    if num > 100:
        return num - 10
    else:
        return mcCarthy91(mcCarthy91(num + 11))
n=int(input("enter number"))
print(mcCarthy91(n))
        