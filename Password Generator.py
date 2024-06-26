import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_strong_password():
    password_length = random.randint(8, 12)
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    # Ensure the password contains at least one uppercase, one lowercase, one digit, and one special character
    while not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or not any(char in string.punctuation for char in password):
        password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.geometry('800x500')
root.title("Strong Password Generator")

# Create GUI elements
generate_button = tk.Button(root, text="Generate Strong Password", command=generate_strong_password)
generate_button.pack(pady=20)

password_entry = tk.Entry(root, width=120, font=('Arial', 32)) # type: ignore
password_entry.pack(pady=10)

# Start the GUI
root.mainloop()