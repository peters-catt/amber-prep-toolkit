# gui_app.py

import tkinter as tk
from tkinter import filedialog, messagebox
from ase.io import read, write
import os

def convert():
    cif_path = filedialog.askopenfilename(title="Select CIF file", filetypes=[("CIF files", "*.cif")])
    if not cif_path:
        return
    output_path = filedialog.asksaveasfilename(title="Save as PDB", defaultextension=".pdb", filetypes=[("PDB files", "*.pdb")])
    if not output_path:
        return

    try:
        atoms = read(cif_path)
        write(output_path, atoms, format='proteindatabank')
        messagebox.showinfo("Success", f"File saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {e}")

app = tk.Tk()
app.title("CIF to PDB Converter")
app.geometry("300x150")

btn = tk.Button(app, text="Convert CIF to PDB", command=convert, padx=10, pady=10)
btn.pack(expand=True)

app.mainloop()
