print('#'* 18)
print("ZEEEEE CALCULATOR")
print('#' * 18)
while True:
    command = input("Enter CALC to calculate, C to clear, OFF to exit: ").upper()
    if command == "OFF":
        print("Calculator turning off...")
        break
    elif command == "C":
        result = 0
        print("Calculator cleared.")
        continue
    elif command == "CALC":

        Z1=float(input("Enter your first number: "))
        Z2=float(input("Enter your second number: "))
        operators = input("Enter (+,-,/,//,**,%): ")
        match operators:
            case "+" :
                answer= Z1+Z2
                print(answer)
            case "-":
                answer=Z1-Z2
                print(answer)
            case "/":
                if Z2==0:
                    print("MATH ERROR")
                else:
                    answer=Z1/Z2
                    print(answer)
            case "//":
                answer= Z1//Z2 
                print(answer)
            case "*":
                answer=Z1*Z2
                print(answer)
            case "**":
                answer= Z1**Z2
                print(answer)
            case "%":
                answer=Z1%Z2
                print(answer)
            case _:
                    print("Invalid Input")
    else:
        print("Invalid Command")
        
    
    


         