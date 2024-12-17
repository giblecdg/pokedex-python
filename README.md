### Pokédex in Python 🐾

Welcome to **Pokédex by giblecdg**, a simple and interactive Pokédex application built with Python and Tkinter! This project allows you to search for your favorite Pokémon, explore their details, and even expand the Pokédex by adding your own entries.  

---
![pokedex tkinter](https://github.com/user-attachments/assets/17f714be-7540-499e-a7b7-04ca0474c14e)
---

### 🌟 Features
- **Search Pokémon**: Find Pokémon by name or ID.
- **Dynamic Interface**: Displays Pokémon details, type, and a short description.
- **Customizable Pokédex**: Add your own Pokémon to the `pokemon_data.json` file and include their sprites in the `sprites` folder.
- **Error Handling**: Gracefully handles typos, special cases, and common search mistakes.

---

### 🔧 Technologies Used
- **Python 3.12.4**
- **Tkinter**: For the graphical user interface.
- **Pillow (PIL)**: To handle Pokémon sprite images.
- **JSON**: To manage Pokémon data.

---

### 📂 Project Structure
```
├── data/
│   └── pokemon_data.json   # JSON file containing Pokémon data
├── images/
│   ├── app/
│   │   ├── gui.png         # GUI background image
│   │   └── icon.ico        # Application icon
│   └── sprites/            # Folder containing Pokémon sprites
├── main.py                 # Main Python script
```

---

### 🚀 How to Use
1. **Install Python 3.12.4** or a compatible version.
2. Install required dependencies using pip:
   ```bash
   pip install pillow
   ```
3. Clone this repository and navigate to the project directory:
   ```bash
   git clone https://github.com/giblecdg/pokedex-python.git
   cd pokedex-python
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Search for a Pokémon by entering its name or ID in the search bar and hit the **SEARCH** button.

---

### 📋 How to Add Pokémon
1. Open the `pokemon_data.json` file in the `data` folder.
2. Add a new Pokémon entry in the following format:
   ```json
   "pokemon_name": [id, "Name", "Type", "Description", "sprite_filename.png"]
   ```
3. Place the corresponding sprite image in the `sprites` folder.

---

### 🐞 Known Issues
- Special characters in Pokémon names (e.g., `Farfetch'd`, `Mr. Mime`) require specific handling.
- Make sure the sprite filenames match exactly with the entries in `pokemon_data.json`.

---

### 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions, improvements, or encounter bugs.

---

### 📜 License
This project is licensed under the MIT License.  
Feel free to use, modify, and distribute it as you like.  

---

### 💬 Credits
Developed with ❤️ by **giblecdg**.  
Enjoy catching 'em all! 🌟
