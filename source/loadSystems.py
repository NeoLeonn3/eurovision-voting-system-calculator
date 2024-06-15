# Imports
from source.load2024 import *
from source.loadYear import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *
from source.classes.system import *

import json
from pathlib import Path

def loadSystems(folderPath, systems):
    try:
        # Create a Path object for the folder
        folder = Path(folderPath)
        if not folder.exists():
            print(f"The folder '{folderPath}' does not exist.")
            return

        # List all files in the specified folder
        files = [f for f in folder.iterdir() if f.is_file()]
        if not files:
            print(f"No files found in the folder '{folderPath}'.")

        # Get the file details
        for file in files:
          with file.open(encoding='utf-8') as tempFile:
            tempJSON = json.load(tempFile)
            # Use file.name to get the file name or str(file) for the full path
            tempSystem = System(tempJSON["name"], tempJSON["description"], file.name)
            systems.append(tempSystem)
            
    except Exception as e:
        print(f"An error occurred: {e}")