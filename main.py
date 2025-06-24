# main.py
import os
import sys
from modules import converter, tleap_generator, utils

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def main_menu():
    while True:
        clear()
        print("=" * 50)
        print("  AMBER Prep Toolkit - Molecular Dynamics Helper")
        print("=" * 50)
        print("1. Convert CIF or mmCIF to PDB")
        print("2. Clean/repair PDB file")
        print("3. Generate tleap input files")
        print("4. Exit")
        print("=" * 50)

        choice = input("Select an option: ")

        if choice == "1":
            converter.convert_to_pdb()
        elif choice == "2":
            converter.clean_pdb()
        elif choice == "3":
            tleap_generator.create_tleap_files()
        elif choice == "4":
            print("Exiting. Goodbye!")
            sys.exit()
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
