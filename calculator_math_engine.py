class MathEngine:
    
    def calculate(self, num1, num2, operation):
        if operation == '1':
            return num1 + num2
        elif operation == '2':
            return num1 - num2
        elif operation == '3':
            return num1 * num2
        elif operation == '4':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 / num2