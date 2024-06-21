# Imports
from source.exportResultsCSV import exportResultsCSV
from source.load2024 import *
from source.loadYear import *
from source.loadSystems import *
from source.inputSelectors import *
from source.display import *
from source.awardPoints import *
from source.exportResultsText import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *
from source.classes.system import *

# Load data from 2024
entries2024 = []
countriesResults2024 = []
rowRanking2024 = []
year2024 = Year(entries2024, countriesResults2024, rowRanking2024)
# print("Loading 2024 data...")
data2024(year2024.entries, year2024.countriesResults, year2024.rowVoteRanking)
# print("Complete!")

# Load data from 2023
entries2023 = []
countriesResults2023 = []
rowRanking2023 = []
year2023 = Year(entries2023, countriesResults2023, rowRanking2023)
# print("Loading 2023 data...")
loadYearData(year2023.entries, year2023.countriesResults, year2023.rowVoteRanking, "2023")
# print("Complete!")

# Load data from 2022
entries2022 = []
countriesResults2022 = []
rowRanking2022 = []
year2022 = Year(entries2022, countriesResults2022, rowRanking2022)
# print("Loading 2022 data...")
loadYearData(year2022.entries, year2022.countriesResults, year2022.rowVoteRanking, "2022")
# print("Complete!")

# Load voting systems
votingSystems = []
# print("Loading voting systems...")
loadSystems('systems', votingSystems)
# print("Complete!")
 
systemSelector = displayVotingSystemMenu(votingSystems)
yearSelector = displayYearMenu()
wantedResults = Results()

# If year selected is 2022
if yearSelector == 2022:
  # Award the points for a year based on a system and return the ranked results to wantedResults 
  awardPoints(year2022, votingSystems[systemSelector].filename, wantedResults)

  while True:
    resSelector = displayRankingsSelector(2022)
    if resSelector in range(0, 3):
      drawRankings(resSelector, 2022, year2022, wantedResults)
    elif (resSelector == 3):
      exportResultsCSV(year2022, wantedResults, yearSelector)
  

elif yearSelector == 2023:
  # Award the points for a year based on a system and return the ranked results to wantedResults 
  awardPoints(year2023, votingSystems[systemSelector].filename, wantedResults)
  
  while True:
    resSelector = displayRankingsSelector(2023)
    if resSelector in range(0, 4):
      drawRankings(resSelector, 2023, year2023, wantedResults)
    elif (resSelector == 4):
      exportResultsCSV(year2023, wantedResults, yearSelector)
      

elif yearSelector == 2024:
  # Award the points for a year based on a system and return the ranked results to wantedResults 
  awardPoints(year2024, votingSystems[systemSelector].filename, wantedResults)

  while True:
    resSelector = displayRankingsSelector(2024)
  
    if resSelector in range(0, 4):
      drawRankings(resSelector, 2024, year2024, wantedResults)
    elif (resSelector == 4):
      exportResultsCSV(year2024, wantedResults, yearSelector)

else:
  print("Unexpected error")

# Export the results to a file


