# Imports
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

# Load data from 2024
entries2024 = []
countriesResults2024 = []
rowRanking2024 = []
year2024 = Year(entries2024, countriesResults2024, rowRanking2024)
print("Loading 2024 data...")
data2024(year2024.entries, year2024.countriesResults, year2024.rowVoteRanking)
print("Complete!")

# Load data from 2023
entries2023 = []
countriesResults2023 = []
rowRanking2023 = []
year2023 = Year(entries2023, countriesResults2023, rowRanking2023)
print("Loading 2023 data...")
loadYearData(year2023.entries, year2023.countriesResults, year2023.rowVoteRanking, "2023")
print("Complete!")

# Load data from 2022
entries2022 = []
countriesResults2022 = []
rowRanking2022 = []
year2022 = Year(entries2022, countriesResults2022, rowRanking2022)
print("Loading 2022 data...")
loadYearData(year2022.entries, year2022.countriesResults, year2022.rowVoteRanking, "2022")
print("Complete!")

# Load voting systems
votingSystems = []
print("Loading voting systems...")
loadSystems('systems', votingSystems)
print("Complete!")

# Print the system details
print("Voting systems available:")
for i in votingSystems:
  print(str(votingSystems.index(i) + 1) + " | Name: " + i.name + " | Description: " + i.description + " | Filename: " + i.filename)
  
systemSelector = getSystemSelection()
yearSelector = getYearSelection()
exportSelector = getExportFileName()
wantedResults = Results()

# If year selected is 2022
if yearSelector == 2022:
  # Award the points for a year based on a system and return the ranked results to wantedResults 
  awardPoints(year2022, votingSystems[systemSelector].filename, wantedResults)

  # Print the results
  print("Total results")
  for i in wantedResults.totalRanking:
    print("Country: " + i[0] + " | Total score: " + str(i[1]))
  
  exportToFile(exportSelector, year2022, wantedResults, yearSelector, votingSystems[systemSelector].name)
  print("Detailed results printed in file " + exportSelector)

elif yearSelector == 2023:
  # Award the points for a year based on a system and return the ranked results to wantedResults 
  awardPoints(year2023, votingSystems[systemSelector].filename, wantedResults)

  # Print the results
  print("Total results (Without the RoW vote)")
  for i in wantedResults.totalRanking:
    print("Country: " + i[0] + " | Total score: " + str(i[1]))

  print("Rest of the World top 10")
  for x in year2023.rowVoteRanking:
    print(str(x[1]) + ") " + x[0])
  
  exportToFile(exportSelector, year2023, wantedResults, yearSelector, votingSystems[systemSelector].name)
  print("Detailed results printed in file " + exportSelector)

elif yearSelector == 2024:
  # Award the points for a year based on a system and return the ranked results to wantedResults 
  awardPoints(year2024, votingSystems[systemSelector].filename, wantedResults)

  # Print the total results
  print("Total results (Without the RoW vote)")
  print("Place | Country | Points")
  for i in wantedResults.totalRanking:
    print(str(wantedResults.totalRanking.index(i) + 1) + " | " + i[0] + " | " + str(i[1]))

  print("Rest of the World top 10")
  for x in year2024.rowVoteRanking:
    print(str(x[1]) + ") " + x[0])
    
  exportToFile(exportSelector, year2024, wantedResults, yearSelector, votingSystems[systemSelector].name)
  print("Detailed results printed in file " + exportSelector)
else:
  print("Unexpected error")

# Export the results to a file


