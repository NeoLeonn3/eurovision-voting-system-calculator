# Imports
from source.load2024 import *
from source.awardPoints import *
from source.classes.entry import *
from source.classes.countryResults import *
from source.classes.year import *

# Load data from 2024
entries2024 = []
countriesResults2024 = []
year2024 = Year(entries2024, countriesResults2024)
print("Loading 2024 data...")
data2024(year2024.entries, year2024.countriesResults)
print("Complete!")

awardPoints(year2024, "current.json")

# for i in year2024.countriesResults:
#   print("Country: " + i.country + " | In Final: " + str(i.inFinal))

