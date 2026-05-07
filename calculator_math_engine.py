class BasicMathEngine:
    
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

class AdvancedMathEngine(BasicMathEngine):
    
    def calculate(self, num1, num2, operation):
        if operation in ('1', '2', '3', '4'):
            return super().calculate(num1, num2, operation)
            
        elif operation == '5':
            return num1 ** num2
        elif operation == '6':
            if num2 == 0:
                raise ZeroDivisionError("Cannot find remainder (modulo) by zero.")
            return num1 % num2 

