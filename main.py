# main.py
from modules import converter

def show_banner():
    print(r"""

      ／＞　 フ
     | 　_　_| 
    ／` ミ＿xノ
   /　　　　 |
  /　 ヽ　　 ﾉ
 │　　|　|　|
／￣|　　 |　|
(￣ヽ＿_ヽ_)__)
＼二)

  「知恵と力を結集せよ」
    — Gather wisdom and strength —

分子動力学ツールキット | Molecular Dynamics Toolkit
卒業研究専用 - 岡部研究 実験補助システム
制作: Weremito Peter

構造変換ツール (CIF ➜ PDB)
PDBクリーニング＆準備
tleap入力ファイル自動生成

Designed to accelerate MD setups using AMBER + VMD + tleap
For researchers working on β-シクロデキストリン and beyond

""")


def main():
    show_banner()
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

