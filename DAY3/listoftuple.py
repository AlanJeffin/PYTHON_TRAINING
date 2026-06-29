tuple_list=eval(input("Enter the list of tuple"))
k=int(input("enter the column"))
product =1
for tup in tuple_list:
    product=product*tup[k]
    print(f"product of values :{k}:{product}")