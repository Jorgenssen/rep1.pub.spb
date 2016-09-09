print("This is fucking Python calculator!")

print("Options:")
print("Enter 'add' to add two numbers")
print("Enter 'subtract' to subtract two numbers")
print("Enter 'multiply' to multiply two numbers")
print("Enter 'divide' to divide two numbers")
print("Enter 'exit' to end the program")

def inputty1():
    print("Do not try to enter any symbols except numbers!!!")
    try:
        num1=float(input("Enter a number: "))
        num2=float(input("Enter a number: "))
        if user_input == "add":
            result=str(num1+num2)
            print("I think you want to see " + result)
        elif user_input == "subtract":
            result=str(num1-num2)
            print("I think you want to see " + result)
        elif user_input == "multiply":
            result=str(num1*num2)
            print("I think you want to see " + result)
        elif user_input == "divide":
            try:
                result=str(num1/num2)
                print("I think you want to see " + result)
            except ZeroDivisionError:
                print("Are you kidding? My school teacher told me it isn't possible to divide on zero")
    except ValueError:
        print("You are stupid little girl! This calculator only for numbers!")
    
while True:    
    user_input=input("What do you want? ")
    if user_input == "exit":
        break
    elif user_input == "add" or user_input == "subtract" or user_input == "multiply" or user_input == "divide":
        inputty1()
    else:
        print("What do you mean?")
