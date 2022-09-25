import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
# print(Path("x/y/test.txt"))
PROJECT_NAME = "DeepClassifier"
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.tst",
    "setup.py",
     "setup.cfg",
     "pyproject.toml",# This file for creating packages
     "toxi.ini",
     "research/.gitkeep",
     "example.ipynb"
    ]

for filepath in list_of_files:
    filedir,filename = os.path.split(filepath)
    if(filedir!=""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the file {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f: 
            pass 
        logging.info(f"creating the empty file {filename}")
    else:
        logging.info(f"File Already Available")

