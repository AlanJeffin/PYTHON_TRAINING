class intToRomanConvertor():
    def int_to_roman(self,num:int):
        symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman=''
        for i in range(len(values)):
            while num>=values[i]:
                roman+=symbols[i]
                num-=values[i]
        return roman
num = int(input("Enter a number: "))
obj=intToRomanConvertor()
print(obj.int_to_roman(num))

        
        
        