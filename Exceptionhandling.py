flag = True
flag2=True
while(flag):
    try:
        Numberator = int(input("Enter Numrator value: "))
        Denominator =int(input("Enter Denominator value: "))  
        result=Numberator/Denominator
        print(result)
        if (Denominator!=0):
            flag=False
        My_List =[2,4,6]
        while(flag2):
            try:
                inputs =int(input("Enter the index: "))
                if (inputs<len(My_List)):
                    flag2=False
                print(My_List[inputs])
            except IndexError:
                print("Indedx value cannot be greater than 2")
    except ZeroDivisionError:
        print("Please enter the Denominator any value but 0")

    