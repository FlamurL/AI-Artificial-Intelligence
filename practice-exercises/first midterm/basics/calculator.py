"""
Write a function that simulates a basic arithmetic calculator. The calculator should interact with the user by reading input from the standard input (command line).

Interaction:

Input: The user will provide input in the following format, all on separate lines:

operand1 (a number)
operator (a character representing the operation)
operand2 (a number)
Processing: The function will take these three inputs, perform the specified calculation, and then print the result to the console.

Supported Operations:

The calculator should support the following operations:

Addition (+)
Subtraction (-)
Multiplication (*)
Integer Division (//) - returns the quotient without the remainder
Division (/) - returns a floating-point quotient
Modulo (Remainder) (%)
Exponentiation (**) - raises operand1 to the power of operand2

"""
operators = ['+', '-', '/', '//', '*', '**', '%']
def calculator():
        operand1 = int(input())
        operator = input()
        operand2 = int(input())

      

        if operator not in operators:
            raise ValueError("Invalid operator")

        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero")
            result = operand1 / operand2
        elif operator == '//':
            if operand2 == 0:
                raise ZeroDivisionError("Integer division by zero")
            result = operand1 // operand2
        elif operator == '%':
            if operand2 == 0:
                raise ZeroDivisionError("Modulo by zero")
            result = operand1 % operand2
        elif operator == '**':
            result = operand1 ** operand2

        print(result)

 


calculator() 