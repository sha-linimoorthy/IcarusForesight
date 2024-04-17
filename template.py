import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "BankruptcyPredictor"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "params.yaml",
    "requirements.txt",
    "app.py",
    "main.py",
    "setup.py",
    "templates/index.html",
    "research/trial.ipynb",
    "Dockerfile"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName = os.path.split(filePath)

    if fileDir!="":
        os.makedirs(fileDir,exist_ok = True)
        logging.info(f"Creating directory: {fileDir} for the file: {filePath}")
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as file:
            pass
            logging.info(f"Created file: {filePath}")
    else:
        logging.info(f"{filePath} already exits")