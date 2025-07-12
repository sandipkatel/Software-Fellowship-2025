import sys

# Basic argument handling
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <name>")
        return
    
    name = sys.argv[1]
    print(f"Hello, {name}!")

# Better argument handling
def calculator():
    if len(sys.argv) != 4:
        print("Usage: python calc.py <num1> <operation> <num2>")
        print("Example: python calc.py 5 + 3")
        return
    
    try:
        num1 = float(sys.argv[1])
        operation = sys.argv[2]
        num2 = float(sys.argv[3])
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        # ... more operations
        
        print(f"Result: {result}")
    except ValueError:
        print("❌ Please enter valid numbers!")

if __name__ == "__main__":
    calculator()