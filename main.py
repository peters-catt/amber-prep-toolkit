# main.py
from modules import converter

def main():
    while True:
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
            print("🚧 Tleap generator not implemented yet.")
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

