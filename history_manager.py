import os
from datetime import datetime

class HistoryManager:
    
    def __init__(self, filename="calculator_history.txt"):
        current_dir = os.path.dirname(__file__)
        self.filepath = os.path.join(current_dir, filename)
        
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as file:
                file.write("=== CALCULATOR HISTORY LOG ===\n\n")

    def save_calculation(self, num1, num2, operation, result):
        symbols = {'1': '+', '2': '-', '3': '*', '4': '/', '5': '^', '6': '%', '7': '√', '8': '!'}
        sym = symbols.get(operation, '?')
        
        timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
        if operation == '7': 
            equation = f"√{num1} = {result}"
        elif operation == '8': 
            equation = f"{int(num1)}! = {result}"
        else: 
            equation = f"{num1} {sym} {num2} = {result}"
        
        with open(self.filepath, 'a', encoding='utf-8') as file:
            file.write(f"[{timestamp}] {equation}\n")

