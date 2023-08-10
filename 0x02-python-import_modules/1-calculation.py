#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def print_operations(a, b):
    """Prints the results of various operations between two numbers."""
    sum_result = add(a, b)
    difference_result = sub(a, b)
    product_result = mul(a, b)
    quotient_result = div(a, b)

    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {difference_result}")
    print(f"{a} * {b} = {product_result}")
    print(f"{a} / {b} = {quotient_result}")

def main():
    """Calculate and print the results of operations between 10 and 5."""
    a = 10
    b = 5
    print_operations(a, b)

if __name__ == "__main__":
    main()
