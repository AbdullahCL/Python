def main():
    z = 0
    a = 0
    
    print("") 
    print("CALCULATOR 1.0.0")
    print("-------------------------------")
    op = ["0: ADD OP.", "1: SUB OP.", "2: MUL OP.", "3: DIV OP.", "4: EXPO OP.", ""] 

    for o in op :
        print(o)     

    a = int(input("Select OP.: "))
   
    if (a in [0, 1, 2, 3, 4]) == False:      
        print("UNKNOW")
        return

    print(op[a])
    print("-------------------------------")
    print("") 
    
    x = int(input("N1: "))
    y = int(input("N2: "))
   
    def switch(m):      
        switcher = {
            0: x + y,
            1: x - y,
            2: x * y,
            3: x / y,
            4: x ** y   
        }
      
        return switcher.get(m)
    
    z = switch(a)
    sign = ["+", "-", "*", "/", "**"]
    print(str(x) + " " + sign[a] + " " + str(y) + " = ", z)

main()
