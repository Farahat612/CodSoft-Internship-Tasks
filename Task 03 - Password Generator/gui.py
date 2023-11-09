import tkinter as tk
import random
import string
import pyperclip  # For clipboard functionality

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_output.config(text=password)
        copy_button.config(state=tk.NORMAL)
    except ValueError as e:
        password_output.config(text="Please enter a valid length.")
        copy_button.config(state=tk.DISABLED)

def copy_to_clipboard():
    generated_password = password_output.cget("text")
    pyperclip.copy(generated_password)

app = tk.Tk()
app.title("Strong Password Generator")
app.geometry("500x300")
app.config(bg="#333333")

header_label = tk.Label(app, text="Password Generator", font=("Arial", 24), bg="#333333", fg="white")
header_label.pack(pady=20)

length_label = tk.Label(app, text="Password Length:", bg="#333333", fg="white", font=("Arial", 14))
length_label.pack()

length_entry = tk.Entry(app, font=("Arial", 14))
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password, bg="#007acc", fg="white", font=("Arial", 14), relief=tk.RAISED, borderwidth=3)
generate_button.pack(pady=20)

password_output = tk.Label(app, text="", bg="#333333", fg="white", font=("Arial", 18), wraplength=400)
password_output.pack()

copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED, bg="#007acc", fg="white", font=("Arial", 14), relief=tk.RAISED, borderwidth=3)
copy_button.pack(pady=10)

app.mainloop()
