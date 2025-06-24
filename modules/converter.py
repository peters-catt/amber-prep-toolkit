# modules/converter.py
from ase.io import read, write
import os

def convert_to_pdb():
    cif_path = input("Enter path to your .cif or .mcif file: ").strip()
    out_pdb = input("Enter output PDB filename (e.g., output.pdb): ").strip()

    try:
        atoms = read(cif_path)  # ASE automatically detects file format
        write(out_pdb, atoms, format='proteindatabank')  # Save as .pdb
        print(f"✅ Successfully converted {cif_path} to {out_pdb}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
    input("Press Enter to return to the main menu...")

def clean_pdb():
    pdb_path = input("Enter path to your PDB file: ").strip()
    cleaned = []
    with open(pdb_path, 'r') as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                cleaned.append(line)

    out_path = f"cleaned_{os.path.basename(pdb_path)}"
    with open(out_path, 'w') as f:
        f.writelines(cleaned)
    print(f"✅ Cleaned PDB written to {out_path}")
    input("Press Enter to return to main menu...")
