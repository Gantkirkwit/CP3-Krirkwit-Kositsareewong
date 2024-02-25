import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_name(input_characters):
    # Convert input characters to a list
    characters = list(input_characters)

    # Generate additional random characters if needed to reach at least 4 letters
    while len(characters) < 4:
        if random.random() < 0.5:  # 50% chance of adding a random letter
            characters.append(random.choice(string.ascii_letters))

    # Shuffle the characters to create a random order
    random.shuffle(characters)

    # Generate one or more numbers to append at the end
    num_digits = random.randint(1, 3)  # Generate 1 to 3 digits
    numbers = ''.join(random.choices(string.digits, k=num_digits))

    # Append numbers at the end
    generated_name = ''.join(characters) + numbers

    return generated_name


def generate_and_display_name():
    # Get user input characters
    input_characters = entry_characters.get()

    # Generate the name
    generated_name = generate_name(input_characters)

    # Display the generated name
    messagebox.showinfo("Generated Name", f"Generated Name: {generated_name}")


# Create Tkinter window
root = tk.Tk()
root.title("Name Generator")

# Create input label and entry for characters
label_characters = tk.Label(root, text="Enter one or more characters:")
label_characters.pack()
entry_characters = tk.Entry(root)
entry_characters.pack()

# Create button to generate and display name
button_generate = tk.Button(root, text="Generate Name", command=generate_and_display_name)
button_generate.pack()


root.mainloop()


