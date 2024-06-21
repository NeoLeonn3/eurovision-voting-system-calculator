import msvcrt
import os
import sys

from source.load2024 import *
from source.loadYear import *
from source.loadSystems import *
from source.inputSelectors import *
from source.awardPoints import *
from source.exportResultsText import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *
from source.classes.system import *

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def drawVotingSystemMenu(selectedOption, selectedDescription, options):
	clearScreen()
	print("+----------------------------------------------------+")
	print("|     Eurovision Song Contest Voting Calculator      |")
	print("+----------------------------------------------------+")
	for i, option in enumerate(options):
		selector = ">" if i == selectedOption else " "
		print(f"{selector} {option}")
	print("\nDescription: ", selectedDescription)  # Display the description
	print("\nUse Arrow Keys to navigate and Enter to select.")

def displayVotingSystemMenu(votingSystems):
	selectedOption = 0
	options = [system.name for system in votingSystems] + ["Exit"]
	selectedDescription = votingSystems[selectedOption].description if votingSystems else "No systems available."  # Get the initial description

	drawVotingSystemMenu(selectedOption, selectedDescription, options)

	while True:
		if os.name == 'nt':  # Windows-specific
			key = msvcrt.getch()
			if key == b'\xe0':  # Special keys (including arrows)
				key = msvcrt.getch()
				if key == b'H':  # Up arrow
					selectedOption = max(0, selectedOption - 1)
				elif key == b'P':  # Down arrow
					selectedOption = min(len(options) - 1, selectedOption + 1)
			elif key == b'\r':  # Enter key
					if selectedOption == len(options) - 1:  # Assuming the last option is Exit
						print("Exiting...")
						clearScreen()
						sys.exit()
					else:
						# print(f"Option {selectedOption + 1} selected.")
						# input("Press Enter to continue...")
						return selectedOption
			selectedDescription = votingSystems[selectedOption].description  if selectedOption < len(votingSystems) else "Exiting the menu."
			drawVotingSystemMenu(selectedOption, selectedDescription, options)
		else:
			print("Arrow key navigation is not supported on this platform.")
			break
	
def drawYearMenu(selectedOption, options):
	clearScreen()
	print("+----------------------------------------------------+")
	print("|     Eurovision Song Contest Voting Calculator      |")
	print("+----------------------------------------------------+")
	for i, option in enumerate(options):
		selector = ">" if i == selectedOption else " "
		print(f"{selector} {option}")
	print("\nUse Arrow Keys to navigate and Enter to select.")
 
# def displayYearMenu where the user selects a year between 2022 and 2024 and returns the selected year as an integer
def displayYearMenu():
	selectedOption = 0
	options = ["2022", "2023", "2024", "Exit"]
	drawYearMenu(selectedOption, options)

	while True:
		if os.name == 'nt':  # Windows-specific
			key = msvcrt.getch()
			if key == b'\xe0':  # Special keys (including arrows)
				key = msvcrt.getch()
				if key == b'H':  # Up arrow
					selectedOption = max(0, selectedOption - 1)
				elif key == b'P':  # Down arrow
					selectedOption = min(len(options) - 1, selectedOption + 1)
			elif key == b'\r':  # Enter key
				if selectedOption == len(options) - 1:  # Assuming the last option is Exit
					print("Exiting...")
					clearScreen()
					sys.exit()
				else:
					# print(f"Option {selectedOption + 1} selected.")
					# input("Press Enter to continue...")
					return int(options[selectedOption])
			drawYearMenu(selectedOption, options)
		else:
			print("Arrow key navigation is not supported on this platform.")
			break
 
# def drawRankingsSelector where the user selects which rankings to show (the options are: Jury, Televote, Total, RoW) 
def drawRankingsSelector(selectedOption, yearSelected):
  if yearSelected < 2023:
    options = ["Jury", "Televote", "Total", "Export all to CSV", "Exit"]
    descriptions = [
      "Shows the rankings based on the jury votes.",
      "Shows the rankings based on the televote.",
      "Shows the total rankings.",
      "Exports all rankings to different CSV files.",
      "Exit the program."
    ]
  else:
    options = ["Jury", "Televote", "Total", "RoW", "Export all to CSV", "Exit"]
    descriptions = [
      "Shows the rankings based on the jury votes.",
      "Shows the rankings based on the televote.",
      "Shows the total rankings.",
      "Shows the Rest of the World rankings.",
      "Exports all rankings to different CSV files.",
      "Exit the program."
    ]
  clearScreen()
  print("+----------------------------------------------------+")
  print("|     Eurovision Song Contest Voting Calculator      |")
  print("+----------------------------------------------------+")
  for i, option in enumerate(options):
    selector = ">" if i == selectedOption else " "
    print(f"{selector} {option}")
    # Display the description
  print("\n", descriptions[selectedOption])
  print("\nUse Arrow Keys to navigate and Enter to select.")
  
# def displayRankingsSelector where the user selects which rankings to show (the options are: Jury, Televote, Total, RoW)
def displayRankingsSelector(yearSelected):
  selectedOption = 0
  options = ["Jury", "Televote", "Total", "RoW", "Export all to CSV", "Exit"]
  drawRankingsSelector(selectedOption, yearSelected)
  while True:
    if os.name == 'nt':  # Windows-specific
      key = msvcrt.getch()
      if key == b'\xe0':  # Special keys (including arrows)
        key = msvcrt.getch()
        if key == b'H':  # Up arrow
          selectedOption = max(0, selectedOption - 1)
        elif key == b'P':  # Down arrow
          selectedOption = min(len(options) - 1, selectedOption + 1)
      elif key == b'\r':  # Enter key
        if selectedOption == len(options) - 1:  # Assuming the last option is Exit
          print("Exiting...")
          clearScreen()
          sys.exit()
        else:
          # print(f"Option {selectedOption + 1} selected.")
          # input("Press Enter to continue...")
          return selectedOption
      drawRankingsSelector(selectedOption, yearSelected)
    else:
      print("Arrow key navigation is not supported on this platform.")
      break

# def drawRankings where depending on the selected option, the program prints the rankings in "Place | Country | Song Name | Song Performer | Points" format
def drawRankings(selectedOption, yearNumber, yearData, results):
  clearScreen()
  print("+----------------------------------------------------+")
  print("|     Eurovision Song Contest Voting Calculator      |")
  print("+----------------------------------------------------+")
  if selectedOption == 0:
    print("Jury Results:")
    print("Place | Country | Song Name | Song Performer | Points")
    for x in results.juryRanking:
      for y in yearData.entries:
        if x[0] == y.country:
          print(str(results.juryRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + " | " + str(x[1]))
  elif selectedOption == 1:
    print("Televote Results:")
    print("Place | Country | Song Name | Song Performer | Points")
    for x in results.televoteRanking:
      for y in yearData.entries:
        if x[0] == y.country:
          print(str(results.televoteRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + " | " + str(x[1]))
  elif selectedOption == 2:
    print("Total Results:")
    print("Place | Country | Song Name | Song Performer | Points")
    for x in results.totalRanking:
      for y in yearData.entries:
        if x[0] == y.country:
          print(str(results.totalRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant + " | " + str(x[1]))
  elif (selectedOption == 3) and (yearNumber > 2022):
    print("Rest of the World Top 10:")
    print("Place | Country | Song Name | Song Performer")
    for x in yearData.rowVoteRanking:
      for y in yearData.entries:
        if x[0] == y.country:
          print(str(yearData.rowVoteRanking.index(x) + 1) + " | " + y.country + " | " + y.song + " | " + y.participant)
  
  else:
    # error message
    print("Exiting...")
    clearScreen()
    sys.exit()
    
  # print "Press Enter to go back"
  input("Press Enter to go back...")
  
  