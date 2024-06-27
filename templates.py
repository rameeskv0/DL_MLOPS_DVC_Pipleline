import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

projectname = "cnnClassifier"

#files needed for cicd-git integration ,telling to create files as mentioning,"config/config.yaml" code is create a config.yaml file in the config folder
list_of_files = [
    ".github/workflows/.gitkeep",
     f"src/{projectname}/__init__.py",     #we are building custom package for our project to import , so we use this constructor
     f"src/{projectname}/components/__init__.py",
     f"src/{projectname}/utils/__init__.py",
     f"src/{projectname}/config/__init__.py",
     f"src/{projectname}/config/configuration.py",
     f"src/{projectname}/pipeline/__init__.py",
     f"src/{projectname}/entity/__init__.py",
     f"src/{projectname}/constants/__init__.py",
     "config/config.yaml",
     "dvc.yaml",
     "params.yaml",
     "requirements.txt",
     "setup.py",
     "research/trials.ipynb",
     "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)     #we gave / in list_of_files,wndows takes \ ,Path function will converts it into windowsPath
    filedir, filename = os.path.split(filepath) # returns 2 objects in a tuple,here conatining .py or other extension will consider as file and rest as directory
    print(filedir,filename)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  #create a directory if filedir is not empty and do not already exist
        logging.info(f"creating directory : {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:       #this will create files (filenames) in the directory created above
            pass
        logging.info(f"creating empty files : {filepath}")
    else:
        logging.info(f"{filename} already created")
        
         