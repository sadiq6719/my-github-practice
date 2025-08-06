def reverse_text(text):
    """
    Reverses the given text string.

    Parameters:
    text (str): The input text to be reversed.

    Returns:
    str: The reversed string, or an error message if input is not valid.
    """
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        
        # Reverse the string using slicing
        return text[::-1]

    except Exception as e:
        return f"Error: {str(e)}"


def simple_calculator(a, b, operator):
    """
    Performs basic arithmetic operations between two numbers.

    Parameters:
    a (float/int): The first number.
    b (float/int): The second number.
    operator (str): The operation to perform: '+', '-', '*', '/'.

    Returns:
    float/int: The result of the calculation, or an error message if input is invalid.
    """
    try:
        # Convert inputs to floats (if not already)
        a = float(a)
        b = float(b)

        # Perform the operation
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        else:
            raise ValueError("Unsupported operator. Use '+', '-', '*', or '/'.")

    except ValueError as ve:
        return f"Value error: {ve}"
    except ZeroDivisionError as zde:
        return f"Math error: {zde}"
    except Exception as e:
        return f"Unexpected error: {e}"
