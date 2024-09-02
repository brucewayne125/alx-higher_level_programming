#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv [3])

    if operator == '+':
        result = add(a, b)
        print(f"{a} {operator} {b} = {result}")
    elif operator == '-':
        result = sub(a, b)
        print(f"{a} {operator} {b} = {result}")
    elif operator == '*':
        result = mul(a, b)
        print(f"{a} {operator} {b} = {result}")
    elif operator == '/':
        result = div(a, b)
        print(f"{a} {operator} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
