from calculator_math_engine import MathEngine

def main():
    print("--- Simple App Calculator ---")
    
    engine = MathEngine()
    
    while True:
        print("\nPlease choose a math operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice not in ('1', '2', '3', '4'):
            print("Error: Invalid choice. Please select 1, 2, 3, or 4.")
            continue
            
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            result = engine.calculate(num1, num2, choice)
            print(f"\nResult: {result}")
            
        except ValueError:
            print("\nError: Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"\nError: {e}")
            
        while True:
            try_again = input("\nDo you want to try again? (yes/no): ").strip().lower()
            if try_again in ('yes', 'y', 'no', 'n'):
                break
            print("Invalid input. Please type 'yes' or 'no'.")
            
        if try_again in ('no', 'n'):
            print("Thank you!")
            break

if __name__ == "__main__":
    main()