def function_with_improved_error_handling(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError as e:
        return f"Error: Invalid input type: {e}"
    except OverflowError as e:
        return f"Error: Overflow error occurred: {e}"
    #Handle more specific exception types as required 

#Example usage
print(function_with_improved_error_handling(10, 2)) # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero
print(function_with_improved_error_handling(10, "hello")) # Output: Error: Invalid input type: unsupported operand type(s) for /: 'int' and 'str'
print(function_with_improved_error_handling(10**1000, 1)) # Output: Error: Overflow error occurred: