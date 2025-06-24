# modules/tleap_generator.py
def create_tleap_files():
    pdb_file = input("Enter path to your cleaned PDB file: ").strip()
    mol_name = input("Enter a molecule name (no spaces): ").strip()
    leapin_name = f"{mol_name}.in"
    
    content = f"""source leaprc.gaff
source leaprc.GLYCAM_06j-1

{mol_name} = loadpdb {pdb_file}
saveamberparm {mol_name} {mol_name}.prmtop {mol_name}.inpcrd
savepdb {mol_name} {mol_name}_tleap.pdb
quit
"""
    with open(leapin_name, 'w') as f:
        f.write(content)
    
    print(f"✅ TLeap input written to {leapin_name}")
    print("Now run: tleap -f", leapin_name)
    input("Press Enter to return to main menu...")
