#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(num):
    """Print the last digit of a number and return it."""
    last_digit = abs(num) % 10
    print(last_digit, end="")
    return last_digit
