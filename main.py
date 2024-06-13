# Imports
from source.load2024 import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *
from source.classes.results import *

# Load data from 2024
entries2024 = []
countriesResults2024 = []
rowRanking2024 = []
wantedResults = Results()
year2024 = Year(entries2024, countriesResults2024, rowRanking2024)
print("Loading 2024 data...")
data2024(year2024.entries, year2024.countriesResults, year2024.rowVoteRanking)
print("Complete!")

# Award the points for a year based on a system and return the ranked results to wantedResults 
awardPoints(year2024, "current.json", wantedResults)

# Print the results
print("Total results (Without the RoW vote)")
for i in wantedResults.totalRanking:
  print("Country: " + i[0] + " | Jury score: " + str(i[1]))
  
print("Rest of the World top 10")
for x in year2024.rowVoteRanking:
  print(str(x[1]) + ") " + x[0])

