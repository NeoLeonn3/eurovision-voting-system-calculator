# Imports
from source.load2024 import *
from source.loadYear import *
from source.loadSystems import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *
from source.classes.system import *

def getSystemSelection():
  while True:
    userInput = input("Please select one of the voting systems available by choosing a number between 1 and 4: ")
    try:
      # Try to convert the input to an integer
      selection = int(userInput)
      # Check if the number is between 1 and 4
      if 1 <= selection <= 4:
        return selection - 1
      else:
        print("Error: Not a valid system option Please try again.")
    except ValueError:
      # Catch the exception if the input is not a number
      print("Error: Invalid input. Please try again.")

def getYearSelection():
  while True:
    userInput = input("Please select the year you want (options: 2022, 2023, 2024): ")
    try:
      # Try to convert the input to an integer
      selection = int(userInput)
      # Check if the number is between 1 and 4
      if 2022 <= selection <= 2024:
        return selection
      else:
        print("Error: Not a valid year option. Please try again.")
    except ValueError:
      # Catch the exception if the input is not a number
      print("Error: Invalid input. Please try again.")
      
def getInput(prompt):
  while True:
    userInput = input(prompt).strip().lower()
    if userInput in ['y', 'n', 'yes', 'no']:
      return userInput
    else:
      print("Error: Invalid input. Please enter 'Y' for yes or 'N' for no.")

def getExportFileName():
  userResponse = getInput("Default filename is 'results.txt'. Do you want to provide a custom filename? (Y/N): ")
  
  if userResponse in ['y', 'yes']:
    filename = input("Please enter the filename: ").strip()
    # Append .txt to the filename if it doesn't have an extension
    if not filename.endswith(".txt"):
      filename += ".txt"
    return filename
  else:
    return "results.txt"