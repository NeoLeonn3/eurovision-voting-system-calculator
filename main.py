# Imports
from source.load2024 import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *

# Load data from 2024
entries2024 = []
countriesResults2024 = []
wantedResults = []
year2024 = Year(entries2024, countriesResults2024)
print("Loading 2024 data...")
data2024(year2024.entries, year2024.countriesResults)
print("Complete!")

# Award the points for a year based on a system and return the ranked results to wantedResults 
awardPoints(year2024, "current.json", wantedResults)

wantedResults = sorted(wantedResults, key=lambda x: x[1], reverse=True)

# Print the results
for i in wantedResults:
  print("Country: " + i[0] + " | Jury score: " + str(i[1]))

