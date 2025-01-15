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
        int or float: The sum of the two values.
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

def say_hi():
    return "hi"

import os
import shutil
from tkinter import Tk, filedialog

# def upload_pdf(destination_folder):
#     """
#     Allows the user to select a PDF file and uploads it to the specified folder.

#     Args:
#         destination_folder (str): The folder where the uploaded PDF will be saved.

#     Returns:
#         str: The path to the uploaded file, or a message if the upload fails.
#     """
#     # Ensure the destination folder exists
#     os.makedirs(destination_folder, exist_ok=True)
    
#     # Initialize Tkinter and hide the root window
#     root = Tk()
#     root.withdraw()
    
#     # Open a file dialog for the user to select a file
#     file_path = filedialog.askopenfilename(
#         title="Select a PDF file",
#         filetypes=[("PDF files", "*.pdf")],
#     )
    
#     if not file_path:
#         return "No file selected."
    
#     # Check if the selected file is a PDF
#     if not file_path.lower().endswith(".pdf"):
#         return "The selected file is not a PDF."

#     try:
#         # Get the file name and copy it to the destination folder
#         file_name = os.path.basename(file_path)
#         destination_path = os.path.join(destination_folder, file_name)
#         shutil.copy(file_path, destination_path)
#         return f"File uploaded successfully to {destination_path}."
#     except Exception as e:
#         return f"An error occurred: {e}"

def welcome():
    return 'welcome new new user'

def finish_unittest():
    return "i finished unit testing"
# Example usage
if __name__ == "__main__":
    # Login example
    print(login("admin", "password123"))  # Expected: Login successful!
    print(login("user", "pass"))          # Expected: Invalid username or password.

    # Sum example
    print(sum_two_values(10, 20))          # Expected: 30
    print(sum_two_values(3.5, 4.5))        # Expected: 8.0




