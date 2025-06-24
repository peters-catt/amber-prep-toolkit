# 🧪 AMBER Prep Toolkit

PythonベースのコマンドラインおよびGUIアプリケーションで、AMBERを使った分子動力学（MD）シミュレーションを効率化します。 Created by **Weremito Peter**.

## ✨ 機能

- .cif または .mmCIF 結晶ファイルを .pdb に変換（ASE使用）
- .pdb ファイルのクリーニングと修復
- AMBER用の tleap.in 入力ファイルを生成
- 分子の可視化（VMD使用、オプション）
- PySimpleGUIを使ったGUI操作

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
```
---

## 🚀 Usage
```bash
#Launch the toolkit with:
python main.py

#You will see a GUI with the following options:
    Convert CIF to PDB
    Clean a PDB file
    Generate tleap input files
    View molecules in VMD (if installed)
```
---

## 🧪 VMD Integration
```bash
#If VMD is installed and available in your PATH, the app will allow you to open .pdb files in VMD for visualization.
#Test VMD installation:
vmd
```
---

## 🗂️ Project Structure
```bash
amber-prep-toolkit/
├── main.py
├── modules/
│   ├── converter.py
│   ├── tleap_generator.py
│   └── utils.py
├── requirements.txt
├── README.md
└── venv/
```
