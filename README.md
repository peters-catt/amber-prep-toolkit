# 🧪 AMBER Prep Toolkit

A Python-based command-line and GUI application to streamline molecular dynamics (MD) simulations using AMBER. Created by **Weremito Peter**.

## ✨ Features

- 🌀 Convert `.cif` or `.mmCIF` crystal files to `.pdb` (using ASE)
- 🧼 Clean and repair `.pdb` files
- 📜 Generate `tleap.in` input files for AMBER
- 🖼️ Visualize molecules using VMD (optional)
- 🖱️ GUI-based operation using PySimpleGUI

---

## ⚙️ Installation

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# If some packages are missing, install them manually:
pip install ase PySimpleGUI

---

## 🚀 Usage

#Launch the toolkit with:
python main.py

#You will see a GUI with the following options:
    Convert CIF to PDB
    Clean a PDB file
    Generate tleap input files
    View molecules in VMD (if installed)

---

## 🧪 VMD Integration
#If VMD is installed and available in your PATH, the app will allow you to open .pdb files in VMD for visualization.
#Test VMD installation:
vmd

---

## 🗂️ Project Structure

amber-prep-toolkit/
├── main.py
├── modules/
│   ├── converter.py
│   ├── tleap_generator.py
│   └── utils.py
├── requirements.txt
├── README.md
└── venv/
