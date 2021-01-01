import math

def main():
    z = 0
    a = 0
    
    print("") 
    print("CALCULATOR 1.0.0")
    print("=====================================")
    op = ["0: ADD OP.", "1: SUB OP.", "2: MUL OP.", "3: DIV OP.", "4: EXPO OP.", "5: ROOT OP.",""] 

    for o in op :
        print(o)     

    a = int(input("Select OP.: "))
   
    if (a in [0, 1, 2, 3, 4, 5]) == False :      
        print("UNKNOW")
        return

    print(op[a])
    print("=====================================")
    print("") 
    
    x = float(input("N1: "))
  
    if (a in [0, 1, 2, 3, 4]) :
        y = float(input("N2: "))
    else:
        y = 2    
   
    def add():
        if (a == 0) :
          return x + y
    
    def sub():
        if (a == 1) :
          return x - y

    def mul():
        if (a == 2) :
          return x * y

    def div():
        if (a == 3) :
          return x / y

    def expo():
        if (a == 4) :
          return x ** y      

    def root():
        if (a == 5) :
          return math.sqrt(x)      

    def switch(m):      
        switcher = {
            0: add(),
            1: sub(),
            2: mul(),
            3: div(),
            4: expo(),
            5: root()
        }
      
        return switcher.get(m)
    
    z = switch(a)
    sign = ["+", "-", "*", "/", "**", "√"]
    print(str(x) + " " + sign[a] + " " + str(y) + " = ", z)
    print("") 
main()
