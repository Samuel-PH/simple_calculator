import math
class Addition:
    def calculate(self, num1, num2):
        return num1 + num2
class Subtraction:
    def calculate(self, num1, num2):
        return num1 - num2
class Multiplication(Addition):

    def calculate(self, num1, num2):
        if num2 >= 0 and num2.is_integer():
            result = 0
            for _ in range(int(num2)):
                result = super().calculate(result, num1)
            return result
        else:
            return num1 * num2
class Division(Subtraction):
    def calculate(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
            
        if num1 >= 0 and num2 > 0 and num1.is_integer() and num2.is_integer():
            quotient = 0
            remainder = num1
            while remainder >= num2:
                remainder = super().calculate(remainder, num2)
                quotient += 1
            if remainder == 0:
                return float(quotient)
        return num1 / num2
    
class AdvancedMathEngine:
    def __init__(self):
        self.adder = Addition()
        self.subtractor = Subtraction()
        self.multiplier = Multiplication()
        self.divider = Division()

    def calculate(self, num1, num2, operation):
        if operation == '1':
            return self.adder.calculate(num1, num2)
        elif operation == '2':
            return self.subtractor.calculate(num1, num2)
        elif operation == '3':
            return self.multiplier.calculate(num1, num2)
        elif operation == '4':
            return self.divider.calculate(num1, num2)
            
        elif operation == '5':
            return num1 ** num2
        elif operation == '6':
            if num2 == 0:
                raise ZeroDivisionError("Cannot find remainder by zero.")
            return num1 % num2
        elif operation == '7':
            if num1 < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            return math.sqrt(num1)
        elif operation == '8':
            if num1 < 0 or not num1.is_integer():
                raise ValueError("Factorial is only defined for non-negative whole numbers.")
            return math.factorial(int(num1))