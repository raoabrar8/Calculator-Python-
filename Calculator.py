def add(x,y):
    return x+y


def substraction(x,y):
    return x-y

    
def multiply(x,y):
    return x*y


def divide(x,y):
    if y ==0:
        return print("invalid entry! Remove 0 from denominator.")
    return x/y


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the seconed number:"))
                
        except ValueError:
            print("Inavlid value, Please try again!")
            continue
        if choice == '1':
            print(f"The Result: {add(num1, num2)}")
            
        elif choice == '2':
            print*(f"The Result: {substraction(num1, num2)}")
            
        elif choice == '3':
            print(f"The Result: {multiply(num1, num2)}")
             
        elif choice == '4':
            print(f"The Result: {divide(num1,num2)}")
            
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    calculator()
        
    
    
    