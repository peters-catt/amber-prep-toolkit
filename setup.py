from setuptools import setup, find_packages

setup(
    name="amber_prep_toolkit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "pymatgen",
        "rdkit-pypi",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': [
            'amberprep=main:main',
        ],
    },
    author="peters-catt",
    description="A toolkit to prepare PDB/CIF files for AMBER MD simulations.",
    url="https://github.com/peters-catt/amber-prep-toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
