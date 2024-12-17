import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

# Function to load Pokémon data with error handling
def load_pokemon_data():
    try:
        with open('data/pokemon_data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Pokemon data file not found.")
        root.destroy()
        exit()
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Pokemon data file is corrupted.")
        root.destroy()
        exit()

# Function to display Pokémon data in the GUI
def display_pokemon_data(pkmn_key):
    try:
        pkmn_data = pokemon_list[pkmn_key]
        id_label.config(text=f"{pkmn_data[0]}", fg="#ffffff", font=("Arial", 12))
        name_label.config(text=f"{pkmn_data[1]}")
        type_label.config(text=f"{pkmn_data[2]}")
        description_label.config(text=f"{pkmn_data[3]}")

        image = Image.open(f"images/sprites/{pkmn_data[4]}").resize((128, 128))
        image_tk = ImageTk.PhotoImage(image)
        pkmn_image.config(image=image_tk)
        pkmn_image.image = image_tk
    except KeyError:
        messagebox.showerror("Error", f"No data found for Pokémon: {pkmn_key}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Image for {pkmn_key} not found.")

# Function to handle Pokémon search
def search_pokemon():
    pkmn_name = entry.get().strip().lower()

    special_cases = {
        "nidoran": lambda: messagebox.showinfo(
            "Info", "For Nidoran♀ type: 'Nidoran F'\nFor Nidoran♂ type: 'Nidoran M'"
        ),
        "nidoranf": lambda: display_pokemon_data("nidoran f"),
        "nidoranm": lambda: display_pokemon_data("nidoran m"),
        "farfetch'd": lambda: display_pokemon_data("farfetchd"),
        "farfetch": lambda: display_pokemon_data("farfetchd"),
        "mr.mime": lambda: display_pokemon_data("mr. mime"),
        "mr mime": lambda: display_pokemon_data("mr. mime"),
        "mrmime": lambda: display_pokemon_data("mr. mime"),
    }

    if pkmn_name in special_cases:
        special_cases[pkmn_name]()
    elif pkmn_name in pokemon_list:
        display_pokemon_data(pkmn_name)
    elif pkmn_name.isdigit():
        pkmn_index = int(pkmn_name) - 1
        if pkmn_index < 0:
            messagebox.showerror("Error", "Pokémon ID must be greater than 0.")
        else:
            try:
                pkmn_key = list(pokemon_list.keys())[pkmn_index]
                display_pokemon_data(pkmn_key)
            except IndexError:
                messagebox.showerror("Error", f"No Pokémon with ID {pkmn_name}.")
    else:
        messagebox.showerror("Error", f"No Pokémon found: '{pkmn_name.capitalize()}'.")

    entry.delete(0, tk.END)

# Initialize main application window
root = tk.Tk()
root.geometry("550x350")
root.title("Pokédex by giblecdg")
root.resizable(False, False)
root.iconbitmap("images/app/icon.ico")

# Load Pokémon data
pokemon_list = load_pokemon_data()

# Create background
background_image = tk.PhotoImage(file="images/app/gui.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create search entry and button
entry = tk.Entry(root, width=25, font=("sans_font", 16), fg="white", bg="#2c2b34", insertbackground="#ffffff")
entry.place(x=340, y=298, width=180)

search_button = tk.Button(root, text="SEARCH", font=("sans_font", 12), fg="white", bg="#2c2b34", command=search_pokemon)
search_button.place(x=40, y=240)

# Create empty labels for Pokémon details
id_label = tk.Label(root, text="", font=("sans_font", 12), fg="#ffffff", bg="#2c2b34")
id_label.place(x=135, y=86)

name_label = tk.Label(root, text="", font=("sans_font", 12), fg="#ffffff", bg="#2c2b34")
name_label.place(x=135, y=122)

type_label = tk.Label(root, text="", font=("sans_font", 12), fg="#ffffff", bg="#2c2b34")
type_label.place(x=133, y=158)

pkmn_image = tk.Label(root, image="", bg="#2c2b34")
pkmn_image.place(x=325, y=110)

description_label = tk.Label(root, text="", font=("sans_font", 7), fg="#ffffff", bg="#2c2b34", wraplength=90)
description_label.place(x=140, y=195)

# Start the Tkinter event loop
root.mainloop()