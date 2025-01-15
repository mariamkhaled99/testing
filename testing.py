def login(username, password):
    """
    Simulates a login function.

    Args:
        username (str): The username for login.
        password (str): The password for login.

    Returns:
        str: Success or failure message.
    """
    if username == "admin" and password == "password123":
        return "Login successful!"
    return "Invalid username or password."

def sum_two_values(a, b):
    """
    Returns the sum of two values.

    Args:
        a (int or float): The first value.
        b (int or float): The second value.

    Returns:
        int or float: The sum of the two values
    """
    return a + b


def generate_even_numbers(start, end):
    """
    Generate a list of even numbers within a given range [start, end].
    
    Parameters:
        start (int): Starting number of the range.
        end (int): Ending number of the range.
    
    Returns:
        list: List of even numbers within the range.
    """
    # Use list comprehension to filter even numbers in the range
    return [num for num in range(start, end + 1) if num % 2 == 0]


def generate_odd_numbers(start, end):
    """
    Generate a list of even numbers within a given range [start, end].
    
    Parameters:
        start (int): Starting number of the range.
        end (int): Ending number of the range.
    
    Returns:
        list: List of even numbers within the range.
    """
    # Use list comprehension to filter even numbers in the range
    return [num for num in range(start, end + 1) if num % 2 != 0]


# Example usage
if __name__ == "__main__":
    # Login example
    print(login("admin", "password123"))  # Expected: Login successful!
    print(login("user", "pass"))          # Expected: Invalid username or password.

    # Sum example
    print(sum_two_values(10, 20))          # Expected: 30
    print(sum_two_values(3.5, 4.5))        # Expected: 8.0




