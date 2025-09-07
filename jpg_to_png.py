import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_dir.delete(0, tk.END)
        entry_dir.insert(0, directory)

def convert_images():
    input_dir = entry_dir.get()
    output_dir = os.path.join(input_dir, "converted")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpeg"):
            img_path = os.path.join(input_dir, filename)
            with Image.open(img_path) as img:
                out_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")
                img.save(out_path, "PNG")
    
    messagebox.showinfo("Conversion", "La conversion est terminée.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur JPEG vers PNG")

# Ajout d'une étiquette et d'un champ de saisie pour le répertoire
tk.Label(root, text="Répertoire des images JPEG:").grid(row=0, column=0, padx=10, pady=10)
entry_dir = tk.Entry(root, width=50)
entry_dir.grid(row=0, column=1, padx=10, pady=10)

# Ajout d'un bouton pour parcourir le répertoire
tk.Button(root, text="Parcourir", command=browse_directory).grid(row=0, column=2, padx=10, pady=10)

# Ajout d'un bouton de conversion
tk.Button(root, text="Convertir", command=convert_images).grid(row=1, column=1, padx=10, pady=10)

# Démarrage de la boucle principale Tkinter
root.mainloop()